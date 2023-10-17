import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()
from api.models import *

topics_data = [
    ["МАКРОЭКОНОМИКА", "macroeconomics"],
    ["РЫНОК ТРУДА", "labor-market"],
    ["ПРЕДПРИНИМАТЕЛЬСТВО", "entrepreneurship"],
    ["РЕГИОНЫ", "regions"],
    ["ЗЕЛЕНАЯ ЭКОНОМИКА", "green-economy"],
    ["НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН", "national-devplan-kazakhstan"],
    ["НАЦИОНАЛЬНЫЕ ПРОЕКТЫ", "national-projects"],
    ["МЕЖДУНАРОДНЫЕ РЕЙТИНГИ", "international-ratings"]
]


economic_indices = [
    ['ВАЛОВЫЙ ВНУТРЕННИЙ ПРОДУКТ (ВВП)', 'gdp', 'МАКРОЭКОНОМИКА'],
    #['РОСТ ВВП ОТДЕЛЬНЫХ СТРАН (В %)', 'gdp_growth', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО)', 'ppi', 'МАКРОЭКОНОМИКА'],
    ['ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА', 'labor-productivity', 'МАКРОЭКОНОМИКА'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ', 'capital-investment', 'МАКРОЭКОНОМИКА'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ ПО ИСТОЧНИКАМ ФИНАНСИРОВАНИЯ', 'capital-investment-financing', 'МАКРОЭКОНОМИКА'],
    ['СТАТИСТИКА ТРУДА ПО СТРАНАМ', 'employment-avunemployment-salary', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', 'consumer-price-index', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ЦЕН НА СОЦИАЛЬНО-ЗНАЧИМЫЕ ПОТРЕБИТЕЛЬСКИЕ ТОВАРЫ', 'cpi-social-consumer-goods', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН ПО СТРАНАМ', 'cpi-by-country', 'МАКРОЭКОНОМИКА'],
    ['МЕЖДУНАРОДНЫЕ РЕЗЕРВЫ И КУРСЫ ВАЛЮТ', 'intreserves-exchange-rates', 'МАКРОЭКОНОМИКА'],
    ['ГОСДОЛГ В % К ВВП ПО СТРАНАМ', 'government-debt-gdp', 'МАКРОЭКОНОМИКА'],
    ['КРЕДИТНЫЙ РЕЙТИНГ', 'credit-rating', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ДОХОДЫ)', 'govbudget-revenue-execution', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ДОХОДЫ)', 'repbudget-revenue-execution', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'govbudget-expenditure-deficit', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'repbudget-expenditure-deficit', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС PMI ПО СТРАНАМ', 'pmi-by-country', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС PMI (В ПРОМЫШЛЕННОСТИ И УСЛУГАХ) ПО СТРАНАМ', 'pmi-industry-country', 'МАКРОЭКОНОМИКА'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН', 'trade-turnover-kazakhstan', 'МАКРОЭКОНОМИКА'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'trade-turnover-kazakhstan-country', 'МАКРОЭКОНОМИКА'],
    ['ЭКСПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'export-kazakhstan-country', 'МАКРОЭКОНОМИКА'],
    ['ИМПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'import-kazakhstan-country', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ ЭКСПОРТНЫЕ ТОВАРЫ', 'major-export-goods', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ ИМПОРТНЫЕ ТОВАРЫ', 'major-import-goods', 'МАКРОЭКОНОМИКА'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'exttrade-structure-kazakhstan', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ НЕСЫРЬЕВЫЕ ЭКСПОРТНЫЕ ТОВАРЫ, $МЛН', 'major-nonrawexport-goods', 'МАКРОЭКОНОМИКА'],
    ['ПРОГНОЗ СОЦИАЛЬНО-ЭКОНОМИЧЕСКОГО РАЗВИТИЯ', 'soceco-development-forecast', 'МАКРОЭКОНОМИКА'],
    ['ПРОГНОЗ ИНСТИТУТА ЭКОНОМИЧЕСКИХ ИССЛЕДОВАНИЙ', 'ier_forecast', 'МАКРОЭКОНОМИКА'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'gdp-oil-forecast', 'МАКРОЭКОНОМИКА'],
    
    
    ['СТАТИСТИКА ТРУДА', 'labor-market-statistics', 'РЫНОК ТРУДА'],
    ['СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)', 'avsalary-economic-activity', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'nominal-wage-index', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'real-wage-index', 'РЫНОК ТРУДА'],
    ['СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'avnominal-salary-region', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'nomwage-index-region', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'realwage-index-region', 'РЫНОК ТРУДА'],
    ['СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'avpercapita-nominal-income', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'nomincome-index-region', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'realincome-index-region', 'РЫНОК ТРУДА'],
    ['ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА', 'popshare-below-povline', 'РЫНОК ТРУДА'],
    
    
    ['ОБЩИЕ ПОКАЗАТЕЛИ', 'general-indicators', 'ПРЕДПРИНИМАТЕЛЬСТВО'],
    ['ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП В 2021 ГОДУ, В %', 'sectoral-specialization', 'ПРЕДПРИНИМАТЕЛЬСТВО'],
    
    
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА', 'rgdp-pvi', 'РЕГИОНЫ'],
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ', 'pcrgdp', 'РЕГИОНЫ'],
    ['ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА', 'agri-forestry-fishery', 'РЕГИОНЫ'],
    ['ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ', 'industrial-production-current', 'РЕГИОНЫ'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА', 'population-beginning-year-kz', 'РЕГИОНЫ'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', 'population-beginning-year', 'РЕГИОНЫ'],
    ['УРБАНИЗАЦИЯ (ДОЛЯ ГОРОДСКОГО К ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ РАСЧЁТНО)', 'urbanization-percent', 'РЕГИОНЫ'],
    
    
    ['ОСНОВНЫЕ ПОКАЗАТЕЛИ В СФЕРЕ НИЗКОУГЛЕРОДНОГО РАЗВИТИЯ И ОКРУЖАЮЩЕЙ СРЕДЫ', 'low-carbon-environment', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМЫ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА 2018 ГОД', 'ghg-emissions-by-country-2018', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['СУММАРНЫЙ ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'ghg-emissions-country-70-18', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ НА ДУШУ НАСЕЛЕНИЯ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'ghg-emissions-popcountry-70-18', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО ОТНОШЕНИЮ К ВВП ПО СТРАНАМ ЗА ПЕРИОД 1990-2018 ГОДА', 'ghg-gdp-percent-90-18', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    
    
    ['СПРАВЕДЛИВАЯ СОЦИАЛЬНАЯ ПОЛИТИКА', 'fair-social-policy', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['ДОСТУПНАЯ И ЭФФЕКТИВНАЯ СИСТЕМА ЗДРАВООХРАНЕНИЯ', 'accessible-effective-healthcare', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['КАЧЕСТВЕННОЕ ОБРАЗОВАНИЕ', 'quality-education', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['СПРАВЕДЛИВОЕ И ЭФФЕКТИВНОЕ ГОСУДАРСТВО НА ЗАЩИТЕ ИНТЕРЕСОВ ГРАЖДАН', 'fair-effective-state', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['НОВАЯ МОДЕЛЬ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'new-public-admin-model', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['КУЛЬТИВИРОВАНИЕ ЦЕННОСТЕЙ ПАТРИОТИЗМА', 'fostering-patriotism', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['УКРЕПЛЕНИЕ НАЦИОНАЛЬНОЙ БЕЗОПАСНОСТИ', 'strengthening-national-security', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['ПОСТРОЕНИЕ ДИВЕРСИФИЦИРОВАННОЙ И ИННОВАЦИОННОЙ ЭКОНОМИКИ', 'diversified-innovative-economy', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['АКТИВНОЕ РАЗВИТИЕ ЭКОНОМИЧЕСКОЙ И ТОРГОВОЙ ДИПЛОМАТИИ', 'active-economic-tradedip', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['СБАЛАНСИРОВАННОЕ ТЕРРИТОРИАЛЬНОЕ РАЗВИТИЕ', 'balanced-regional-development', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    
    
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "УСТОЙЧИВЫЙ ЭКОНОМИЧЕСКИЙ РОСТ, НАПРАВЛЕННЫЙ НА ПОВЫШЕНИЕ БЛАГОСОСТОЯНИЯ КАЗАХСТАНЦЕВ"', 'sustainable-growth-project', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ ПО РАЗВИТИЮ ПРЕДПРИНИМАТЕЛЬСТВА ', 'entrepreneurship-project', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "СИЛЬНЫЕ РЕГИОНЫ - ДРАЙВЕР РАЗВИТИЯ СТРАНЫ"', 'strong-regions-project', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ХОД РЕАЛИЗАЦИИ ПРОЕКТА "АУЫЛ - ЕЛ БЕСІГІ"', 'aulelbesig-project-progress', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ БЮДЖЕТНЫЙ КРЕДИТ НА ПРИОБРЕТЕНИЕ ЖИЛЬЯ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'housing-credit-specialists', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ ПОДЪЕМНОЕ ПОСОБИЕ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'supplementary-allowance-specialists', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    
    
    ['РЕЙТИНГ МИРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd-competitiveness-ranking', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['РЕЙТИНГ ЦИФРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd-digital-competitiveness', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['РЕЙТИНГ ПО КАЧЕСТВУ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'government-quality-ranking', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС СОЦИАЛЬНОГО ПРОГРЕССА', 'social-progress-index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ЧЕЛОВЕЧЕСКОГО РАЗВИТИЯ ПРООН', 'hdi-undp', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ВОСПРИЯТИЯ КОРРУПЦИИ', 'corruption-perception-index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ЭКОНОМИЧЕСКОЙ СВОБОДЫ', 'economic-freedom-index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ВЕРХОВЕНСТВА ЗАКОНА', 'rule-law-index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ГЛОБАЛЬНЫЙ ИНДЕКС ИННОВАЦИЙ', 'global-innovation-index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ']
]


table_info = [
    ['ВАЛОВЫЙ ВНУТРЕННИЙ ПРОДУКТ (ВВП)', 'gdp'],
    #['РОСТ ВВП ОТДЕЛЬНЫХ СТРАН (В %)', 'gdp_growth'],
    ['ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО)', 'ppi'],
    ['ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА', 'labor_productivity'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ', 'capital_investment'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ ПО ИСТОЧНИКАМ ФИНАНСИРОВАНИЯ', 'capital_investment_financing'],
    ['СТАТИСТИКА ТРУДА ПО СТРАНАМ', 'employment_unemployment_average_salary'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', 'consumer_price_index1'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', 'consumer_price_index2'],
    ['ИНДЕКС ЦЕН НА СОЦИАЛЬНО-ЗНАЧИМЫЕ ПОТРЕБИТЕЛЬСКИЕ ТОВАРЫ', 'cpi_social_consumer_goods'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН ПО СТРАНАМ', 'cpi_by_country'],
    ['МЕЖДУНАРОДНЫЕ РЕЗЕРВЫ И КУРСЫ ВАЛЮТ', 'international_reserves_exchange_rates1'],
    ['МЕЖДУНАРОДНЫЕ РЕЗЕРВЫ И КУРСЫ ВАЛЮТ', 'international_reserves_exchange_rates2'],
    ['ГОСДОЛГ В % К ВВП ПО СТРАНАМ', 'government_debt_to_gdp'],
    ['КРЕДИТНЫЙ РЕЙТИНГ', 'credit_rating'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ДОХОДЫ)', 'government_budget_revenue_execution'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ДОХОДЫ)', 'republican_budget_revenue_execution'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'government_budget_expenditure_deficit'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'republican_budget_expenditure_deficit'],
    ['ИНДЕКС PMI ПО СТРАНАМ', 'pmi_by_country'],
    ['ИНДЕКС PMI (В ПРОМЫШЛЕННОСТИ И УСЛУГАХ) ПО СТРАНАМ', 'pmi_industry_services_by_country'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН', 'trade_turnover_kazakhstan'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'trade_turnover_by_country_kazakhstan'],
    ['ЭКСПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'export_kazakhstan_by_country'],
    ['ИМПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'import_kazakhstan_by_country'],
    ['ОСНОВНЫЕ ЭКСПОРТНЫЕ ТОВАРЫ', 'major_export_goods'],
    ['ОСНОВНЫЕ ИМПОРТНЫЕ ТОВАРЫ', 'major_import_goods'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'external_trade_structure_kazakhstan_in_million_usd1'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'external_trade_structure_kazakhstan_in_million_usd2'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'external_trade_structure_kazakhstan_in_million_usd3'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'external_trade_structure_kazakhstan_in_million_usd4'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'external_trade_structure_kazakhstan_in_million_usd5'],
    ['ОСНОВНЫЕ НЕСЫРЬЕВЫЕ ЭКСПОРТНЫЕ ТОВАРЫ, $МЛН', 'major_non_raw_export_goods_in_million_usd1'],
    ['ОСНОВНЫЕ НЕСЫРЬЕВЫЕ ЭКСПОРТНЫЕ ТОВАРЫ, $МЛН', 'major_non_raw_export_goods_in_million_usd2'],
    ['ПРОГНОЗ СОЦИАЛЬНО-ЭКОНОМИЧЕСКОГО РАЗВИТИЯ', 'socio_economic_development_forecast'],
    ['ПРОГНОЗ ИНСТИТУТА ЭКОНОМИЧЕСКИХ ИССЛЕДОВАНИЙ', 'institute_of_economic_research_forecast'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'consensus_gdp_growth_and_oil_prices_forecast1'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'consensus_gdp_growth_and_oil_prices_forecast2'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'consensus_gdp_growth_and_oil_prices_forecast3'],
    
    
    ['СТАТИСТИКА ТРУДА', 'labor_market_statistics'],
    ['СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)', 'average_salary_by_economic_activity_in_thousand_tenge'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'nominal_wage_index'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'real_wage_index'],
    ['СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'average_nominal_salary_by_region_in_thousand_tenge'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'nominal_wage_index_by_region'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'real_wage_index_by_region'],
    ['СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'average_per_capita_nominal_income_by_region_in_tenge'],
    ['ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'nominal_income_index_by_region'],
    ['ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'real_income_index_by_region'],
    ['ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА', 'population_share_below_poverty_line'],
    
    
    ['ОБЩИЕ ПОКАЗАТЕЛИ', 'general_indicators1'],
    ['ОБЩИЕ ПОКАЗАТЕЛИ', 'general_indicators2'],
    ['ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП В 2021 ГОДУ, В %', 'sectoral_specialization_msp_2021_percentage'],
    
    
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА', 'regional_gross_domestic_product_and_physical_volume_index'],
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ', 'per_capita_regional_gross_domestic_product'],
    ['ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА', 'output_of_agricultural_forestry_and_fishery_production'],
    ['ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ', 'industrial_production_volume_at_current_prices'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year_kz'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year1'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year2'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year3'],
    ['УРБАНИЗАЦИЯ (ДОЛЯ ГОРОДСКОГО К ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ РАСЧЁТНО)', 'urbanization_as_percentage_of_total_population_estimate'],
    
    
    ['ОСНОВНЫЕ ПОКАЗАТЕЛИ В СФЕРЕ НИЗКОУГЛЕРОДНОГО РАЗВИТИЯ И ОКРУЖАЮЩЕЙ СРЕДЫ', 'low_carbon_development_and_environmental_indicators'],
    ['ОБЪЕМЫ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА 2018 ГОД', 'greenhouse_gas_emissions_by_country_2018'],
    ['СУММАРНЫЙ ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'total_greenhouse_gas_emissions_by_country_1970_2018'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ НА ДУШУ НАСЕЛЕНИЯ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'greenhouse_gas_emissions_per_capita_by_country_1970_2018'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО ОТНОШЕНИЮ К ВВП ПО СТРАНАМ ЗА ПЕРИОД 1990-2018 ГОДА', 'greenhouse_gas_emissions_as_percentage_of_gdp_by_country_1990_2018'],
    
    
    ['СПРАВЕДЛИВАЯ СОЦИАЛЬНАЯ ПОЛИТИКА', 'fair_social_policy'],
    ['ДОСТУПНАЯ И ЭФФЕКТИВНАЯ СИСТЕМА ЗДРАВООХРАНЕНИЯ', 'accessible_and_effective_healthcare_system'],
    ['КАЧЕСТВЕННОЕ ОБРАЗОВАНИЕ', 'quality_education'],
    ['СПРАВЕДЛИВОЕ И ЭФФЕКТИВНОЕ ГОСУДАРСТВО НА ЗАЩИТЕ ИНТЕРЕСОВ ГРАЖДАН', 'fair_and_effective_state_protecting_citizens_interests'],
    ['НОВАЯ МОДЕЛЬ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'new_model_of_public_administration'],
    ['КУЛЬТИВИРОВАНИЕ ЦЕННОСТЕЙ ПАТРИОТИЗМА', 'fostering_patriotism'],
    ['УКРЕПЛЕНИЕ НАЦИОНАЛЬНОЙ БЕЗОПАСНОСТИ', 'strengthening_national_security'],
    ['ПОСТРОЕНИЕ ДИВЕРСИФИЦИРОВАННОЙ И ИННОВАЦИОННОЙ ЭКОНОМИКИ', 'diversified_and_innovative_economy'],
    ['АКТИВНОЕ РАЗВИТИЕ ЭКОНОМИЧЕСКОЙ И ТОРГОВОЙ ДИПЛОМАТИИ', 'active_economic_and_trade_diplomacy'],
    ['СБАЛАНСИРОВАННОЕ ТЕРРИТОРИАЛЬНОЕ РАЗВИТИЕ', 'balanced_regional_development'],
    
    
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "УСТОЙЧИВЫЙ ЭКОНОМИЧЕСКИЙ РОСТ, НАПРАВЛЕННЫЙ НА ПОВЫШЕНИЕ БЛАГОСОСТОЯНИЯ КАЗАХСТАНЦЕВ"', 'sustainable_economic_growth_project'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ ПО РАЗВИТИЮ ПРЕДПРИНИМАТЕЛЬСТВА ', 'entrepreneurship_development_project'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "СИЛЬНЫЕ РЕГИОНЫ - ДРАЙВЕР РАЗВИТИЯ СТРАНЫ"', 'strong_regions_as_driver_of_country_development_project'],
    ['ХОД РЕАЛИЗАЦИИ ПРОЕКТА "АУЫЛ - ЕЛ БЕСІГІ"', 'aul_el_besig_project_progress'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ БЮДЖЕТНЫЙ КРЕДИТ НА ПРИОБРЕТЕНИЕ ЖИЛЬЯ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'specialists_receiving_budgetary_housing_credit'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ ПОДЪЕМНОЕ ПОСОБИЕ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'specialists_receiving_supplementary_allowance'],
    
    
    ['РЕЙТИНГ МИРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd_global_competitiveness_ranking'],
    ['РЕЙТИНГ ЦИФРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd_digital_competitiveness_ranking'],
    ['РЕЙТИНГ ПО КАЧЕСТВУ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'government_quality_ranking'],
    ['ИНДЕКС СОЦИАЛЬНОГО ПРОГРЕССА', 'social_progress_index'],
    ['ИНДЕКС ЧЕЛОВЕЧЕСКОГО РАЗВИТИЯ ПРООН', 'human_development_index_undp'],
    ['ИНДЕКС ВОСПРИЯТИЯ КОРРУПЦИИ', 'corruption_perception_index'],
    ['ИНДЕКС ЭКОНОМИЧЕСКОЙ СВОБОДЫ', 'economic_freedom_index'],
    ['ИНДЕКС ВЕРХОВЕНСТВА ЗАКОНА', 'rule_of_law_index'],
    ['ГЛОБАЛЬНЫЙ ИНДЕКС ИННОВАЦИЙ', 'global_innovation_index']
]

def delete_all():
    Table.objects.all().delete()
    Economic_index.objects.all().delete()
    Topic.objects.all().delete()


def insert_topics(topics_data):
    for topic in topics_data:
        insert_topic = Topic(name=topic[0], slug=topic[1])
        insert_topic.save()


def insert_economic_indices(economic_indices):
    for index in economic_indices:
        topic = Topic.objects.get(name=index[2])
        insert_index = Economic_index(name=index[0], slug=index[1], macro_topic=topic)
        insert_index.save()


def insert_tables(table_info):
    for table in table_info:
        economic_index = Economic_index.objects.get(name=table[0])
        table = Table(path=table[1], macro_economic_index=economic_index)
        table.save()


def update_topics():
    delete_all()
    insert_topics(topics_data)
    insert_economic_indices(economic_indices)
    insert_tables(table_info)