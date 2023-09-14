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
    ['ВАЛОВЫЙ ВНУТРЕННИЙ ПРОДУКТ (ВВП)', 'gdp.xlsx', 'МАКРОЭКОНОМИКА'],
    ['РОСТ ВВП ОТДЕЛЬНЫХ СТРАН (В %)', 'gdp_growth.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА (ИФО)', 'ppi.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ПРОИЗВОДИТЕЛЬНОСТЬ ТРУДА', 'labor_productivity.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ', 'capital_investment.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ ПО ИСТОЧНИКАМ ФИНАНСИРОВАНИЯ', 'capital_investment_financing.xlsx', 'МАКРОЭКОНОМИКА'],
    ['СТАТИСТИКА ТРУДА ПО СТРАНАМ', 'employment_unemployment_average_salary.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН И ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ', 'cpi_ppi.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ЦЕН НА СОЦИАЛЬНО-ЗНАЧИМЫЕ ПОТРЕБИТЕЛЬСКИЕ ТОВАРЫ', 'cpi_social_consumer_goods.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН ПО СТРАНАМ', 'cpi_by_country.xlsx', 'МАКРОЭКОНОМИКА'],
    ['МЕЖДУНАРОДНЫЕ РЕЗЕРВЫ И КУРСЫ ВАЛЮТ', 'international_reserves_exchange_rates.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ГОСДОЛГ В % К ВВП ПО СТРАНАМ', 'government_debt_to_gdp.xlsx', 'МАКРОЭКОНОМИКА'],
    ['КРЕДИТНЫЙ РЕЙТИНГ', 'credit_rating.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ДОХОДЫ)', 'government_budget_revenue_execution.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ДОХОДЫ)', 'republican_budget_revenue_execution.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'government_budget_expenditure_deficit.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИСПОЛНЕНИЕ РЕСПУБЛИКАНСКОГО БЮДЖЕТА (ЗАТРАТЫ И ДЕФИЦИТ)', 'republican_budget_expenditure_deficit.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС PMI ПО СТРАНАМ', 'pmi_by_country.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИНДЕКС PMI (В ПРОМЫШЛЕННОСТИ И УСЛУГАХ) ПО СТРАНАМ', 'pmi_industry_services_by_country.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН', 'trade_turnover_kazakhstan.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ТОРГОВЫЙ ОБОРОТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'trade_turnover_by_country_kazakhstan.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ЭКСПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'export_kazakhstan_by_country.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ИМПОРТ РЕСПУБЛИКИ КАЗАХСТАН В РАЗРЕЗЕ СТРАН', 'import_kazakhstan_by_country.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ ЭКСПОРТНЫЕ ТОВАРЫ', 'major_export_goods.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ ИМПОРТНЫЕ ТОВАРЫ', 'major_import_goods.xlsx', 'МАКРОЭКОНОМИКА'],
    ['СТРУКТУРА ВНЕШНЕЙ ТОРГОВЛИ РЕСПУБЛИКИ КАЗАХСТАН В $МЛН', 'external_trade_structure_kazakhstan_in_million_usd.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ОСНОВНЫЕ НЕСЫРЬЕВЫЕ ЭКСПОРТНЫЕ ТОВАРЫ, $МЛН', 'major_non_raw_export_goods_in_million_usd.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ПРОГНОЗ СОЦИАЛЬНО-ЭКОНОМИЧЕСКОГО РАЗВИТИЯ', 'socio_economic_development_forecast.xlsx', 'МАКРОЭКОНОМИКА'],
    ['ПРОГНОЗ ИНСТИТУТА ЭКОНОМИЧЕСКИХ ИССЛЕДОВАНИЙ', 'institute_of_economic_research_forecast.xlsx', 'МАКРОЭКОНОМИКА'],
    ['КОНСЕНСУС ПРОГНОЗ РОСТА ВВП КАЗАХСТАНА И ДРУГИХ СТРАН (%) И ЦЕН НА НЕФТЬ ($/БАРРЕЛЬ)', 'consensus_gdp_growth_and_oil_prices_forecast.xlsx', 'МАКРОЭКОНОМИКА'],
    
    
    ['СТАТИСТИКА ТРУДА', 'labor_market_statistics.xlsx', 'РЫНОК ТРУДА'],
    ['СРЕДНЕМЕСЯЧНАЯ ЗАРАБОТНАЯ ПЛАТА ПО ВИДАМ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ (В ТЫС. ТЕНГЕ)', 'average_salary_by_economic_activity_in_thousand_tenge.xlsx', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'nominal_wage_index.xlsx', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ', 'real_wage_index.xlsx', 'РЫНОК ТРУДА'],
    ['СРЕДНЕМЕСЯЧНАЯ НОМИНАЛЬНАЯ ЗАРАБОТНАЯ ПЛАТА (В ТЫС. ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'average_nominal_salary_by_region_in_thousand_tenge.xlsx', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'nominal_wage_index_by_region.xlsx', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНОЙ ЗАРАБОТНОЙ ПЛАТЫ В РАЗРЕЗЕ РЕГИОНОВ', 'real_wage_index_by_region.xlsx', 'РЫНОК ТРУДА'],
    ['СРЕДНЕДУШЕВЫЕ НОМИНАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ НАСЕЛЕНИЯ (В ТЕНГЕ) В РАЗРЕЗЕ РЕГИОНОВ', 'average_per_capita_nominal_income_by_region_in_tenge.xlsx', 'РЫНОК ТРУДА'],
    ['ИНДЕКС НОМИНАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'nominal_income_index_by_region.xlsx', 'РЫНОК ТРУДА'],
    ['ИНДЕКС РЕАЛЬНЫХ ДЕНЕЖНЫХ ДОХОДОВ В РАЗРЕЗЕ РЕГИОНОВ', 'real_income_index_by_region.xlsx', 'РЫНОК ТРУДА'],
    ['ДОЛЯ НАСЕЛЕНИЯ, ИМЕЮЩЕГО ДОХОДЫ НИЖЕ ВЕЛИЧИНЫ ПРОЖИТОЧНОГО МИНИМУМА', 'population_share_below_poverty_line.xlsx', 'РЫНОК ТРУДА'],
    
    
    ['ОБЩИЕ ПОКАЗАТЕЛИ', 'general_indicators.xlsx', 'ПРЕДПРИНИМАТЕЛЬСТВО'],
    ['ОТРАСЛЕВАЯ СПЕЦИАЛИЗАЦИЯ СУБЪЕКТОВ МСП В 2021 ГОДУ, В %', 'sectoral_specialization_msp_2021_percentage.xlsx', 'ПРЕДПРИНИМАТЕЛЬСТВО'],
    
    
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ И ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА', 'regional_gross_domestic_product_and_physical_volume_index.xlsx', 'РЕГИОНЫ'],
    ['ВАЛОВЫЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ НА ДУШУ НАСЕЛЕНИЯ', 'per_capita_regional_gross_domestic_product.xlsx', 'РЕГИОНЫ'],
    ['ВАЛОВЫЙ ВЫПУСК ПРОДУКЦИИ (УСЛУГ) СЕЛЬСКОГО, ЛЕСНОГО И РЫБНОГО ХОЗЯЙСТВА', 'output_of_agricultural_forestry_and_fishery_production.xlsx', 'РЕГИОНЫ'],
    ['ОБЪЕМЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА В ДЕЙСТВУЮЩИХ ЦЕНАХ', 'industrial_production_volume_at_current_prices.xlsx', 'РЕГИОНЫ'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ РЕСПУБЛИКИ КАЗАХСТАН НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year_kz.xlsx', 'РЕГИОНЫ'],
    ['ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ НА НАЧАЛО ГОДА', 'population_at_the_beginning_of_the_year.xlsx', 'РЕГИОНЫ'],
    ['УРБАНИЗАЦИЯ (ДОЛЯ ГОРОДСКОГО К ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ РАСЧЁТНО)', 'urbanization_as_percentage_of_total_population_estimate.xlsx', 'РЕГИОНЫ'],
    
    
    ['ОСНОВНЫЕ ПОКАЗАТЕЛИ В СФЕРЕ НИЗКОУГЛЕРОДНОГО РАЗВИТИЯ И ОКРУЖАЮЩЕЙ СРЕДЫ', 'low_carbon_development_and_environmental_indicators.xlsx', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМЫ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА 2018 ГОД', 'greenhouse_gas_emissions_by_country_2018.xlsx', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['СУММАРНЫЙ ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'total_greenhouse_gas_emissions_by_country_1970_2018.xlsx', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ НА ДУШУ НАСЕЛЕНИЯ ПО СТРАНАМ ЗА ПЕРИОД 1970-2018 ГОДА', 'greenhouse_gas_emissions_per_capita_by_country_1970_2018.xlsx', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    ['ОБЪЕМ ВЫБРОСОВ ПАРНИКОВЫХ ГАЗОВ ПО ОТНОШЕНИЮ К ВВП ПО СТРАНАМ ЗА ПЕРИОД 1990-2018 ГОДА', 'greenhouse_gas_emissions_as_percentage_of_gdp_by_country_1990_2018.xlsx', 'ЗЕЛЕНАЯ ЭКОНОМИКА'],
    
    
    ['СПРАВЕДЛИВАЯ СОЦИАЛЬНАЯ ПОЛИТИКА', 'fair_social_policy.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['ДОСТУПНАЯ И ЭФФЕКТИВНАЯ СИСТЕМА ЗДРАВООХРАНЕНИЯ', 'accessible_and_effective_healthcare_system.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['КАЧЕСТВЕННОЕ ОБРАЗОВАНИЕ', 'quality_education.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['СПРАВЕДЛИВОЕ И ЭФФЕКТИВНОЕ ГОСУДАРСТВО НА ЗАЩИТЕ ИНТЕРЕСОВ ГРАЖДАН', 'fair_and_effective_state_protecting_citizens_interests.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['НОВАЯ МОДЕЛЬ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'new_model_of_public_administration.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['КУЛЬТИВИРОВАНИЕ ЦЕННОСТЕЙ ПАТРИОТИЗМА', 'fostering_patriotism.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['УКРЕПЛЕНИЕ НАЦИОНАЛЬНОЙ БЕЗОПАСНОСТИ', 'strengthening_national_security.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['ПОСТРОЕНИЕ ДИВЕРСИФИЦИРОВАННОЙ И ИННОВАЦИОННОЙ ЭКОНОМИКИ', 'diversified_and_innovative_economy.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['АКТИВНОЕ РАЗВИТИЕ ЭКОНОМИЧЕСКОЙ И ТОРГОВОЙ ДИПЛОМАТИИ', 'active_economic_and_trade_diplomacy.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    ['СБАЛАНСИРОВАННОЕ ТЕРРИТОРИАЛЬНОЕ РАЗВИТИЕ', 'balanced_regional_development.xlsx', 'НАЦИОНАЛЬНЫЙ ПЛАН РАЗВИТИЯ РЕСПУБЛИКИ КАЗАХСТАН'],
    
    
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "УСТОЙЧИВЫЙ ЭКОНОМИЧЕСКИЙ РОСТ, НАПРАВЛЕННЫЙ НА ПОВЫШЕНИЕ БЛАГОСОСТОЯНИЯ КАЗАХСТАНЦЕВ"', 'sustainable_economic_growth_project.xlsx', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ ПО РАЗВИТИЮ ПРЕДПРИНИМАТЕЛЬСТВА ', 'entrepreneurship_development_project.xlsx', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['НАЦИОНАЛЬНЫЙ ПРОЕКТ "СИЛЬНЫЕ РЕГИОНЫ - ДРАЙВЕР РАЗВИТИЯ СТРАНЫ"', 'strong_regions_as_driver_of_country_development_project.xlsx', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ХОД РЕАЛИЗАЦИИ ПРОЕКТА "АУЫЛ - ЕЛ БЕСІГІ"', 'aul_el_besig_project_progress.xlsx', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ БЮДЖЕТНЫЙ КРЕДИТ НА ПРИОБРЕТЕНИЕ ЖИЛЬЯ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'specialists_receiving_budgetary_housing_credit.xlsx', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    ['ИНФОРМАЦИЯ О СПЕЦИАЛИСТАХ, ПОЛУЧИВШИХ ПОДЪЕМНОЕ ПОСОБИЕ В РАМКАХ ПРОЕКТА "С ДИПЛОМОМ В СЕЛО" (ТЫС. ТЕНГЕ)', 'specialists_receiving_supplementary_allowance.xlsx', 'НАЦИОНАЛЬНЫЕ ПРОЕКТЫ'],
    
    
    ['РЕЙТИНГ МИРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd_global_competitiveness_ranking.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['РЕЙТИНГ ЦИФРОВОЙ КОНКУРЕНТОСПОСОБНОСТИ IMD', 'imd_digital_competitiveness_ranking.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['РЕЙТИНГ ПО КАЧЕСТВУ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ', 'government_quality_ranking.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС СОЦИАЛЬНОГО ПРОГРЕССА', 'social_progress_index.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ЧЕЛОВЕЧЕСКОГО РАЗВИТИЯ ПРООН', 'human_development_index_undp.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ВОСПРИЯТИЯ КОРРУПЦИИ', 'corruption_perception_index.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ЭКОНОМИЧЕСКОЙ СВОБОДЫ', 'economic_freedom_index.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ИНДЕКС ВЕРХОВЕНСТВА ЗАКОНА', 'rule_of_law_index.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ'],
    ['ГЛОБАЛЬНЫЙ ИНДЕКС ИННОВАЦИЙ', 'global_innovation_index.xlsx', 'МЕЖДУНАРОДНЫЕ РЕЙТИНГИ']
]


def delete_all():
    Economic_index.objects.all().delete()
    Topic.objects.all().delete()


def insert_topics(topics_data):
    for topic in topics_data:
        insert_topic = Topic(name=topic)
        insert_topic.save()


def insert_economic_indices(economic_indices):
    for index in economic_indices:
        topic = Topic.objects.get(name=index[2])
        insert_index = Economic_index(name=index[0], path=index[1], macro_topic=topic)
        insert_index.save()


def update_topics():
    delete_all()
    insert_topics(topics_data)
    insert_economic_indices(economic_indices)
