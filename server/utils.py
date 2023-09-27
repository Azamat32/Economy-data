import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()
from api.models import *

topics_data = [
    "МАКРОЭКОНОМИКА",
    "РЫНОК ТРУДА",
    "ПРЕДПРИНИМАТЕЛЬСТВО",
    "РЕГИОНЫ",
    "ЗЕЛЕНАЯ ЭКОНОМИКА",
    "НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН",
    "НАЦИОНАЛЬНЫЕ ПРОЕКТЫ",
    "МЕЖДУНАРОДНЫЕ РЕЙТИНГИ",
]


economic_indices = [
    ['ВАЛОВЫЙ ВНУТРЕННИЙ ПРОДУКТ (ВВП)', 'gdp', 'МАКРОЭКОНОМИКА'],
    #['РОСТ ВВП ОТДЕЛЬНЫХ СТРАН (В %)', 'gdp_growth', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО)', 'ppi', 'МАКРОЭКОНОМИКА'],
    ['ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА', 'labor_productivity', 'МАКРОЭКОНОМИКА'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ', 'capital_investment', 'МАКРОЭКОНОМИКА'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ ПО ИСТОЧНИКАМ ФИНАНСИРОВАНИЯ', 'capital_investment_financing', 'МАКРОЭКОНОМИКА'],
    ['СТАТИСТИКА ТРУДА ПО СТРАНАМ', 'employment_unemployment_average_salary', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', 'consumer_price_index1', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', 'consumer_price_index2', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ЦЕН НА СОЦИАЛЬНО-ЗНАЧИМЫЕ ПОТРЕБИТЕЛЬСКИЕ ТОВАРЫ', 'cpi_social_consumer_goods', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН ПО СТРАНАМ', 'cpi_by_country', 'МАКРОЭКОНОМИКА'],
    ['МЕЖДУНАРОДНЫЕ РЕЗЕРВЫ И КУРСЫ ВАЛЮТ', 'international_reserves_exchange_rates1', 'МАКРОЭКОНОМИКА'],
    ['МЕЖДУНАРОДНЫЕ РЕЗЕРВЫ И КУРСЫ ВАЛЮТ', 'international_reserves_exchange_rates2', 'МАКРОЭКОНОМИКА'],
    ['ГОСДОЛГ В % К ВВП ПО СТРАНАМ', 'government_debt_to_gdp', 'МАКРОЭКОНОМИКА'],
    ['КРЕДИТНЫЙ РЕЙТИНГ', 'credit_rating', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ДОХОДЫ)', 'government_budget_revenue_execution', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ДОХОДЫ)', 'republican_budget_revenue_execution', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'government_budget_expenditure_deficit', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'republican_budget_expenditure_deficit', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС PMI ПО СТРАНАМ', 'pmi_by_country', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС PMI (В ПРОМЫШЛЕННОСТИ И УСЛУГАХ) ПО СТРАНАМ', 'pmi_industry_services_by_country', 'МАКРОЭКОНОМИКА'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН', 'trade_turnover_kazakhstan', 'МАКРОЭКОНОМИКА'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'trade_turnover_by_country_kazakhstan', 'МАКРОЭКОНОМИКА'],
    ['ЭКСПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'export_kazakhstan_by_country', 'МАКРОЭКОНОМИКА'],
    ['ИМПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'import_kazakhstan_by_country', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ ЭКСПОРТНЫЕ ТОВАРЫ', 'major_export_goods', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ ИМПОРТНЫЕ ТОВАРЫ', 'major_import_goods', 'МАКРОЭКОНОМИКА'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'external_trade_structure_kazakhstan_in_million_usd', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ НЕСЫРЬЕВЫЕ ЭКСПОРТНЫЕ ТОВАРЫ, $МЛН', 'major_non_raw_export_goods_in_million_usd1', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ НЕСЫРЬЕВЫЕ ЭКСПОРТНЫЕ ТОВАРЫ, $МЛН', 'major_non_raw_export_goods_in_million_usd2', 'МАКРОЭКОНОМИКА'],
    ['ПРОГНОЗ СОЦИАЛЬНО-ЭКОНОМИЧЕСКОГО РАЗВИТИЯ', 'socio_economic_development_forecast', 'МАКРОЭКОНОМИКА'],
    ['ПРОГНОЗ ИНСТИТУТА ЭКОНОМИЧЕСКИХ ИССЛЕДОВАНИЙ', 'institute_of_economic_research_forecast', 'МАКРОЭКОНОМИКА'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'consensus_gdp_growth_and_oil_prices_forecast1', 'МАКРОЭКОНОМИКА'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'consensus_gdp_growth_and_oil_prices_forecast2', 'МАКРОЭКОНОМИКА'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'consensus_gdp_growth_and_oil_prices_forecast3', 'МАКРОЭКОНОМИКА'],
    
    
    ['СТАТИСТИКА ТРУДА', 'labor_market_statistics', 'РЫНОК ТРУДА'],
    ['СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)', 'average_salary_by_economic_activity_in_thousand_tenge', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'nominal_wage_index', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'real_wage_index', 'РЫНОК ТРУДА'],
    ['СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'average_nominal_salary_by_region_in_thousand_tenge', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'nominal_wage_index_by_region', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'real_wage_index_by_region', 'РЫНОК ТРУДА'],
    ['СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'average_per_capita_nominal_income_by_region_in_tenge', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'nominal_income_index_by_region', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'real_income_index_by_region', 'РЫНОК ТРУДА'],
    ['ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА', 'population_share_below_poverty_line', 'РЫНОК ТРУДА'],
    
    
    ['ОБЩИЕ ПОКАЗАТЕЛИ', 'general_indicators', 'ПРЕДПРИНИМАТЕЛЬСТВО'],
    ['ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП В 2021 ГОДУ, В %', 'sectoral_specialization_msp_2021_percentage', 'ПРЕДПРИНИМАТЕЛЬСТВО'],
    
    
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА', 'regional_gross_domestic_product_and_physical_volume_index', 'РЕГИОНЫ'],
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ', 'per_capita_regional_gross_domestic_product', 'РЕГИОНЫ'],
    ['ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА', 'output_of_agricultural_forestry_and_fishery_production', 'РЕГИОНЫ'],
    ['ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ', 'industrial_production_volume_at_current_prices', 'РЕГИОНЫ'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year_kz', 'РЕГИОНЫ'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year', 'РЕГИОНЫ'],
    ['УРБАНИЗАЦИЯ (ДОЛЯ ГОРОДСКОГО К ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ РАСЧЁТНО)', 'urbanization_as_percentage_of_total_population_estimate', 'РЕГИОНЫ'],
    
    
    ['ОСНОВНЫЕ ПОКАЗАТЕЛИ В СФЕРЕ НИЗКОУГЛЕРОДНОГО РАЗВИТИЯ И ОКРУЖАЮЩЕЙ СРЕДЫ', 'low_carbon_development_and_environmental_indicators', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМЫ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА 2018 ГОД', 'greenhouse_gas_emissions_by_country_2018', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['СУММАРНЫЙ ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'total_greenhouse_gas_emissions_by_country_1970_2018', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ НА ДУШУ НАСЕЛЕНИЯ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'greenhouse_gas_emissions_per_capita_by_country_1970_2018', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО ОТНОШЕНИЮ К ВВП ПО СТРАНАМ ЗА ПЕРИОД 1990-2018 ГОДА', 'greenhouse_gas_emissions_as_percentage_of_gdp_by_country_1990_2018', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    
    
    ['СПРАВЕДЛИВАЯ СОЦИАЛЬНАЯ ПОЛИТИКА', 'fair_social_policy', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['ДОСТУПНАЯ И ЭФФЕКТИВНАЯ СИСТЕМА ЗДРАВООХРАНЕНИЯ', 'accessible_and_effective_healthcare_system', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['КАЧЕСТВЕННОЕ ОБРАЗОВАНИЕ', 'quality_education', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['СПРАВЕДЛИВОЕ И ЭФФЕКТИВНОЕ ГОСУДАРСТВО НА ЗАЩИТЕ ИНТЕРЕСОВ ГРАЖДАН', 'fair_and_effective_state_protecting_citizens_interests', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['НОВАЯ МОДЕЛЬ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'new_model_of_public_administration', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['КУЛЬТИВИРОВАНИЕ ЦЕННОСТЕЙ ПАТРИОТИЗМА', 'fostering_patriotism', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['УКРЕПЛЕНИЕ НАЦИОНАЛЬНОЙ БЕЗОПАСНОСТИ', 'strengthening_national_security', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['ПОСТРОЕНИЕ ДИВЕРСИФИЦИРОВАННОЙ И ИННОВАЦИОННОЙ ЭКОНОМИКИ', 'diversified_and_innovative_economy', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['АКТИВНОЕ РАЗВИТИЕ ЭКОНОМИЧЕСКОЙ И ТОРГОВОЙ ДИПЛОМАТИИ', 'active_economic_and_trade_diplomacy', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['СБАЛАНСИРОВАННОЕ ТЕРРИТОРИАЛЬНОЕ РАЗВИТИЕ', 'balanced_regional_development', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    
    
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "УСТОЙЧИВЫЙ ЭКОНОМИЧЕСКИЙ РОСТ, НАПРАВЛЕННЫЙ НА ПОВЫШЕНИЕ БЛАГОСОСТОЯНИЯ КАЗАХСТАНЦЕВ"', 'sustainable_economic_growth_project', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ ПО РАЗВИТИЮ ПРЕДПРИНИМАТЕЛЬСТВА ', 'entrepreneurship_development_project', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "СИЛЬНЫЕ РЕГИОНЫ - ДРАЙВЕР РАЗВИТИЯ СТРАНЫ"', 'strong_regions_as_driver_of_country_development_project', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ХОД РЕАЛИЗАЦИИ ПРОЕКТА "АУЫЛ - ЕЛ БЕСІГІ"', 'aul_el_besig_project_progress', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ БЮДЖЕТНЫЙ КРЕДИТ НА ПРИОБРЕТЕНИЕ ЖИЛЬЯ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'specialists_receiving_budgetary_housing_credit', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ ПОДЪЕМНОЕ ПОСОБИЕ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'specialists_receiving_supplementary_allowance', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    
    
    ['РЕЙТИНГ МИРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd_global_competitiveness_ranking', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['РЕЙТИНГ ЦИФРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd_digital_competitiveness_ranking', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['РЕЙТИНГ ПО КАЧЕСТВУ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'government_quality_ranking', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС СОЦИАЛЬНОГО ПРОГРЕССА', 'social_progress_index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ЧЕЛОВЕЧЕСКОГО РАЗВИТИЯ ПРООН', 'human_development_index_undp', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ВОСПРИЯТИЯ КОРРУПЦИИ', 'corruption_perception_index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ЭКОНОМИЧЕСКОЙ СВОБОДЫ', 'economic_freedom_index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ВЕРХОВЕНСТВА ЗАКОНА', 'rule_of_law_index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ГЛОБАЛЬНЫЙ ИНДЕКС ИННОВАЦИЙ', 'global_innovation_index', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ']
]


def delete_all():
    Table.objects.all().delete()
    Economic_index.objects.all().delete()
    Topic.objects.all().delete()


def insert_topics(topics_data):
    for topic in topics_data:
        insert_topic = Topic(name=topic)
        insert_topic.save()


def insert_economic_indices(economic_indices):
    for index in economic_indices:
        topic = Topic.objects.get(name=index[2])
        if not Economic_index.objects.filter(name=index[0]).exists():
            insert_index = Economic_index(name=index[0], macro_topic=topic)
            insert_index.save()


def insert_tables(economic_indices):
    for index in economic_indices:
        economic_index = Economic_index.objects.get(name=index[0])
        table = Table(path=index[1], macro_economic_index=economic_index)
        table.save()


def update_topics():
    delete_all()
    insert_topics(topics_data)
    insert_economic_indices(economic_indices)
    insert_tables(economic_indices)
