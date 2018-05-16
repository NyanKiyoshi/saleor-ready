from decimal import Decimal

import pytest
from collections import namedtuple

from prices import Money

from saleor.core.templatetags.taxed_prices import price

Request = namedtuple('Request', ('taxes', ))


@pytest.mark.parametrize(
    'include_taxes_in_prices, display_gross_prices, expected_price', (
        (False, False, Decimal('10.00')),
        (False, True, Decimal('12.30')),
        (True, False, Decimal('8.13')),
        (True, True, Decimal('10.00')),
    )
)
def test_price_forced_handles_vat(
        product, taxes, site_settings,
        include_taxes_in_prices, display_gross_prices, expected_price):
    """
    Feature introduced by PR #9:
        force to show a single price from a Product/ ProductVariant as taxed
    """

    site_settings.include_taxes_in_prices = include_taxes_in_prices
    site_settings.display_gross_prices = display_gross_prices
    site_settings.save()

    ctx = {
        'request': Request(taxes=taxes), 'site': site_settings.site}
    taxed_price = price(
        ctx, product.price, force_taxed=True, force_from=product)['price']

    assert isinstance(taxed_price, Money)
    assert taxed_price.amount == expected_price
