import re

data = [
    "HARTFORD SPRINGFIELD-CT - - 225 - -",
    "HAYWARD - CA - 350 - - -",
    # ... (all other lines from the table)
]

parsed_data = []
for line in data:
    parts = line.split(" - ")
    name = parts[0].strip()
    shipping_usa_match = re.search(r'(\d+)', line)
    shipping_usa = int(shipping_usa_match.group()) if shipping_usa_match else None
    if shipping_usa is not None:
        parsed_data.append({'name': name, 'shipping_USA': shipping_usa, 'shipping_ocean': 1000})

print(parsed_data)

# if request.method == 'POST':
#     auction_form = AuctionForm(request.POST)
#     if auction_form.is_valid():
#         selected_auction = auction_form.cleaned_data['sale_location']
#     else:
#         selected_auction = None
# else:
#     auction_form = AuctionForm()
#     selected_auction = None
#
# if request.method == 'POST':
#     engine_form = EngineForm(request.POST)
#     if engine_form.is_valid():
#         selected_engine = engine_form.cleaned_data['operation']
#     else:
#         selected_engine = None
# else:
#     engine_form = EngineForm()
#     selected_engine = None
#
#
# if request.method == 'POST':
#     auction_price_form = AuctionPriceForm(request.POST)
#     if auction_price_form.is_valid():
#         auction_price = int(auction_price_form.cleaned_data['auction_price'])
#     else:
#         auction_price = 0
# else:
#     auction_price_form = AuctionPriceForm()
#     auction_price = 0
#
# if selected_auction == "Copart":
#     if request.method == 'POST':
#         sale_location_form = CalculatorFormCopart(request.POST)
#         if sale_location_form.is_valid():
#             selected_sale_location = 0
#         else:
#             selected_sale_location = None
#     else:
#         sale_location_form = CalculatorFormCopart()
#         selected_sale_location = None
# elif selected_auction == "IAAI":
#     if request.method == 'POST':
#         sale_location_form = CalculatorFormIAAI(request.POST)
#         if sale_location_form.is_valid():
#             selected_sale_location = 0
#         else:
#             selected_sale_location = None
#     else:
#         sale_location_form = CalculatorFormIAAI()
#         selected_sale_location = None
# else:
#     sale_location_form = CalculatorFormCopart()
#     selected_sale_location = None


def calculator(request):
    sales_locations_Copart = SaleLocationCopard.objects.all()
    sales_locations_IAAI = SaleLocationIAAI.objects.all()
    calculate_form = CalculateForm()
    selected_location = None
    auction_tax = 0
    engine_tax = 0
    import_duty = 0
    vat = 0
    if request.method == 'POST':
        calculate_form = CalculateForm(request.POST)
        if calculate_form.is_valid():
            auction_type = request.POST.get('auction_field')
            fuel_type = request.POST.get('fuel_field')
            auction_price = int(request.POST.get('auction_price'))
            engine_field = (request.POST.get('engine_field'))
            engine_field = engine_field.replace(',', '.')
            engine = float(engine_field)
            year = int(request.POST.get('year_field'))
            current_year = datetime.datetime.now().year
            age = current_year - year
            euro_dollar = 1.13
            if auction_type == 'Copart':
                selected_location = get_object_or_404(SaleLocationCopard, name=request.POST.get('copart_location'))
                if auction_price <= 49:
                    auction_tax = 79 + 10 + 1 + 0
                elif auction_price <= 99:
                    auction_tax = 79 + 10 + 1 + 0
                elif auction_price <= 199:
                    auction_tax = 79 + 10 + 25 + 39
                elif auction_price <= 299:
                    auction_tax = 79 + 10 + 50 + 39
                elif auction_price <= 399:
                    auction_tax = 79 + 10 + 75 + 39
                elif auction_price <= 499:
                    auction_tax = 79 + 10 + 110 + 39
                elif auction_price <= 549:
                    auction_tax = 79 + 10 + 125 + 49
                elif auction_price <= 599:
                    auction_tax = 79 + 10 + 130 + 49
                elif auction_price <= 699:
                    auction_tax = 79 + 10 + 140 + 49
                elif auction_price <= 799:
                    auction_tax = 79 + 10 + 155 + 49
                elif auction_price <= 899:
                    auction_tax = 79 + 10 + 170 + 49
                elif auction_price <= 999:
                    auction_tax = 79 + 10 + 185 + 49
                elif auction_price <= 1199:
                    auction_tax = 79 + 10 + 200 + 69
                elif auction_price <= 1299:
                    auction_tax = 79 + 10 + 225 + 69
                elif auction_price <= 1399:
                    auction_tax = 79 + 10 + 240 + 69
                elif auction_price <= 1499:
                    auction_tax = 79 + 10 + 250 + 69
                elif auction_price <= 1599:
                    auction_tax = 79 + 10 + 260 + 79
                elif auction_price <= 1699:
                    auction_tax = 79 + 10 + 275 + 79
                elif auction_price <= 1799:
                    auction_tax = 79 + 10 + 285 + 79
                elif auction_price <= 1999:
                    auction_tax = 79 + 10 + 300 + 79
                elif auction_price <= 2399:
                    auction_tax = 79 + 10 + 325 + 89
                elif auction_price <= 2499:
                    auction_tax = 79 + 10 + 335 + 89
                elif auction_price <= 2999:
                    auction_tax = 79 + 10 + 350 + 89
                elif auction_price <= 3499:
                    auction_tax = 79 + 10 + 400 + 89
                elif auction_price <= 3999:
                    auction_tax = 79 + 10 + 450 + 89
                elif auction_price <= 4499:
                    auction_tax = 79 + 10 + 575 + 99
                elif auction_price <= 4999:
                    auction_tax = 79 + 10 + 600 + 99
                elif auction_price <= 5999:
                    auction_tax = 79 + 10 + 625 + 99
                elif auction_price <= 7499:
                    auction_tax = 79 + 10 + 650 + 119
                elif auction_price <= 7999:
                    auction_tax = 79 + 10 + 675 + 119
                elif auction_price <= 9999:
                    auction_tax = 79 + 10 + 675 + 129
                elif auction_price <= 14999:
                    auction_tax = 79 + 10 + 700 + 129
                elif auction_price <= 100000:
                    auction_tax = 79 + 10 + ((auction_price / 100) * 5.5) + 129
            elif auction_type == 'IAAI':
                selected_location = get_object_or_404(SaleLocationIAAI, name=request.POST.get('iaai_location'))
                if auction_price <= 99:
                    auction_tax = 79 + 35 + 45 + 0
                elif auction_price <= 199:
                    auction_tax = 79 + 35 + 80 + 39
                elif auction_price <= 399:
                    auction_tax = 79 + 35 + 120 + 39
                elif auction_price <= 499:
                    auction_tax = 79 + 35 + 170 + 39
                elif auction_price <= 599:
                    auction_tax = 79 + 35 + 195 + 49
                elif auction_price <= 699:
                    auction_tax = 79 + 35 + 225 + 49
                elif auction_price <= 799:
                    auction_tax = 79 + 35 + 245 + 49
                elif auction_price <= 899:
                    auction_tax = 79 + 35 + 265 + 49
                elif auction_price <= 999:
                    auction_tax = 79 + 35 + 290 + 49
                elif auction_price <= 1099:
                    auction_tax = 79 + 35 + 340 + 69
                elif auction_price <= 1199:
                    auction_tax = 79 + 35 + 355 + 69
                elif auction_price <= 1299:
                    auction_tax = 79 + 35 + 370 + 69
                elif auction_price <= 1399:
                    auction_tax = 79 + 35 + 385 + 69
                elif auction_price <= 1499:
                    auction_tax = 79 + 35 + 400 + 69
                elif auction_price <= 1599:
                    auction_tax = 79 + 35 + 415 + 79
                elif auction_price <= 1699:
                    auction_tax = 79 + 35 + 430 + 79
                elif auction_price <= 1799:
                    auction_tax = 79 + 35 + 445 + 79
                elif auction_price <= 1999:
                    auction_tax = 79 + 35 + 460 + 79
                elif auction_price <= 2199:
                    auction_tax = 79 + 35 + 480 + 89
                elif auction_price <= 2399:
                    auction_tax = 79 + 35 + 495 + 89
                elif auction_price <= 2599:
                    auction_tax = 79 + 35 + 510 + 89
                elif auction_price <= 2799:
                    auction_tax = 79 + 35 + 525 + 89
                elif auction_price <= 2999:
                    auction_tax = 79 + 35 + 550 + 89
                elif auction_price <= 3499:
                    auction_tax = 79 + 35 + 650 + 89
                elif auction_price <= 3999:
                    auction_tax = 79 + 35 + 700 + 89
                elif auction_price <= 4499:
                    auction_tax = 79 + 35 + 725 + 99
                elif auction_price <= 4999:
                    auction_tax = 79 + 35 + 750 + 99
                elif auction_price <= 5999:
                    auction_tax = 79 + 35 + 775 + 99
                elif auction_price <= 6999:
                    auction_tax = 79 + 35 + 800 + 119
                elif auction_price <= 7999:
                    auction_tax = 79 + 35 + 825 + 119
                elif auction_price <= 9999:
                    auction_tax = 79 + 35 + 850 + 129
                elif auction_price <= 14999:
                    auction_tax = 79 + 35 + 900 + 129
                elif auction_price <= 1000000:
                    auction_tax = 79 + 35 + ((auction_price/100) * 7.5) + 129

            if fuel_type == 'Бензин':
                if engine <= 3:
                    engine_tax = 50 * age * engine * euro_dollar
                elif engine > 3:
                    engine_tax = 100 * age * engine * euro_dollar

                import_duty = round((auction_price + auction_tax + 1000) * 0.1)
                vat = round((auction_price + auction_tax + engine_tax + import_duty + 1000) * 0.2)

            elif fuel_type == 'Дизель':
                if engine <= 3.5:
                    engine_tax = 75 * age * engine * euro_dollar
                elif engine > 3.5:
                    engine_tax = 150 * age * engine * euro_dollar

                import_duty = round((auction_price + auction_tax + 1000) * 0.1)
                vat = round((auction_price + auction_tax + engine_tax + import_duty + 1000) * 0.2)

            elif fuel_type == 'Електро':
                engine_tax = 1 * engine * euro_dollar
                import_duty = 0
                vat = 0

            shipping_services = 1100
            brokerage_services = 100
            shipping_USA = selected_location.shipping_USA
            shipping_ocean = selected_location.shipping_ocean
            dealer_fee = 100
            user_fee = 300
            shipping_to_europe = shipping_USA + shipping_ocean + dealer_fee + user_fee

        return redirect('result',
                            auction_type=auction_type,
                            fuel_type=fuel_type,
                            engine_field=engine_field,
                            year=year,
                            engine_tax=engine_tax,
                            auction_price=auction_price,
                            selected_location=selected_location,
                            auction_tax=auction_tax,
                            shipping_ocean=shipping_ocean,
                            shipping_USA=shipping_USA,
                            shipping_to_europe=shipping_to_europe,
                            import_duty=import_duty,
                            vat=vat,
                            shipping_services=shipping_services,
                            brokerage_services=brokerage_services)

    context = {'sales_locations_Copart': sales_locations_Copart,
               'sales_locations_IAAI': sales_locations_IAAI,
               'calculate_form': calculate_form,
               'selected_location': selected_location,
               }
    return render(request, "usdp/calculator.html", context=context)


def result(request, auction_type, fuel_type, auction_price, engine_field,
           year, engine_tax, selected_location, auction_tax, shipping_ocean,
           shipping_USA, shipping_to_europe,
           import_duty, vat, shipping_services, brokerage_services):

    context = {
        'auction_type': auction_type,
        'fuel_type': fuel_type,
        'auction_price': auction_price,
        'selected_location': selected_location,
        'auction_tax': auction_tax,
        'shipping_ocean': shipping_ocean,
        'shipping_USA': shipping_USA,
        'shipping_to_europe': shipping_to_europe,
        'engine_field': engine_field,
        'year': year,
        'engine_tax': engine_tax,
        'import_duty': import_duty,
        'vat': vat,
        'shipping_services': shipping_services,
        'brokerage_services': brokerage_services
    }
    return render(request, 'usdp/result.html', context=context)
