from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EconomicIndex, Topic
from .serializer import  EconomicIndexSerializer, TopicSerializer, EconomicIndicesSerializer
from django.http import JsonResponse
import json

def populate_data():
    content_data = [
    ("Макроэкономика"),
    ("Рынок труда"),
    ("Предпринимательство"),
    ("Регионы"),
    ("Зеленая Экономика"),
    ("Национальный план развития Республики Казахстан"),
    ("Национальные проекты"),
    ("Международные рейтинги"),
    ]

    indicators_data = [
    (1, "Валовый внутренний продукт (ВВП)", "Link 1", 1),
    (2, "Индекс физического объема (ИФО)", "Link 2", 1),
    (3, "Производительность труда", "Link 3", 1),
    (4, "Инвестиции в основной капитал", "Link 4", 1),
    (5, "Занятость, безработица, средняя зарплата по основным странам", "Link 5", 1),
    (6, "Индекс потребительских цен и индекс цен производителей", "Link 6", 1),
    (7, "Индекс цен на социально-значимые потребительские товары", "Link 7", 1),
    (8, "Индекс потребительских цен по странам", "Link 8", 1),
    (9, "Международные резервы и курсы валют", "Link 9", 1),
    (10, "Госдолг в % к ВВП по странам", "Link 10", 1),
    (11, "Кредитный рейтинг", "Link 11", 1),
    (12, "Исполнение государственного/республиканского бюджета (доходы)", "Link 12", 1),
    (13, "Исполнение государственного/республиканского бюджета (затраты)", "Link 13", 1),
    (14, "Индекс PMI по странам", "Link 14", 1),
    (15, "Торговый оборот Республики Казахстан", "Link 15", 1),
    (16, "Экспорт/импорт Республики Казахстан в разрезе стран", "Link 16", 1),
    (17, "Основные экспортные/импортные товары", "Link 17", 1),
    (18, "Структура внешней торговли Республики Казахстан", "Link 18", 1),
    (19, "Основные экспортные несырьевые товары", "Link 19", 1),
    (20, "Прогноз социально-экономического развития", "Link 20", 1),
    (21, "Прогноз Института экономических исследований", "Link 21", 1),
    (22, "Консенсус прогноз", "Link 22", 1),
    (23, "Статистика труда", "Link 23", 2),
    (24, "Среднемесячная номинальная заработная плата по ВЭД", "Link 24", 2),
    (25, "Индекс номинальной заработной платы по ВЭД", "Link 25", 2),
    (26, "Индекс реальной заработной платы по ВЭД", "Link 26", 2),
    (27, "Среднемесячная номинальная заработная плата в разрезе регионов", "Link 27", 2),
    (28, "Индекс номинальной/реальной заработной платы в разрезе регионов", "Link 28", 2),
    (29, "Среднедушевые номинальные денежные доходы населения", "Link 29", 2),
    (30, "Индекс номинальных/реальных денежных доходов в разрезе регионов", "Link 30", 2),
    (31, "Доля населения, имеющего доходы ниже величины прожиточного минимума", "Link 31", 2),
    (32, "Общие показатели", "Link 32", 3),
    (33, "Отраслевая специализация субъектов МСП", "Link 33", 3),
    (34, "Валовый региональный продукт и индекс физического объема", "Link 34", 4),
    (35, "Валовый региональный продукт на душу населения", "Link 35", 4),
    (36, "Валовый выпуск продукции (услуг) сельского, лесного и рыбного хозяйства", "Link 36", 4),
    (37, "Объемы промышленного производства", "Link 37", 4),
    (38, "Численность населения Республики Казахстан", "Link 38", 4),
    (39, "Численность населения на начало года", "Link 39", 4),
    (40, "Численность населения на начало года", "Link 40", 4),
    (41, "Основные показатели в сфере низкоуглеродного развития и окружающей среды", "Link 41", 5),
    (42, "Объемы выбросов парниковых газов по странам", "Link 42", 5),
    (43, "Справедливая социальная политика", "Link 43", 6),
    (44, "Качественное образование", "Link 44", 6),
    (45, "Доступная и эффективная система здравоохранения", "Link 45", 6),
    (46, "Справедливое и эффективное государство на защите интересов граждан", "Link 46", 6),
    (47, "Новая модель государственного управления", "Link 47", 6),
    (48, "Культивирование ценностей патриотизма", "Link 48", 6),
    (49, "Укрепление национальной безопасности", "Link 49", 6),
    (50, "Построение диверсифицированной и инновационной экономики", "Link 50", 6),
    (51, "Активное развитие экономической и торговой дипломатии", "Link 51", 6),
    (52, "Сбалансированное территориальное развитие", "Link 52", 6),
    (53, "Устойчивый экономический рост, направленный на повышение благосостояния казахстанцев", "Link 53", 7),
    (54, "По развитию предпринимательства", "Link 54", 7),
    (55, "Сильные регионы - драйвер развития страны", "Link 55", 7),
    (56, 'Ход реализации проекта "Ауыл - Ел бесігі"', "Link 56", 7),
    (57, 'Информация о специалистах. получивших бюджетный кредит на приобретение жилья в рамках Проекта "С дипломом в село"', "Link 57", 7),
    (58, 'Информация о специалистах. получивших подъемное пособие в рамках проекта "С дипломом в село"', "Link 58", 7),
    (59, "Международные рейтинги", "Link 59", 8),
]

    for topic_name in content_data:
        topic, created = Topic.objects.get_or_create(name=topic_name.upper())
        if created:
            print(f"Создана тема: {topic_name}")
        else:
            print(f"Тема уже существует: {topic_name}")

    for index_id, index_name, index_link, topic_id in indicators_data:
        topic = Topic.objects.get(name=content_data[topic_id - 1].upper())
        index_name_upper = index_name.upper()
        economic_index, created = EconomicIndex.objects.get_or_create(
            id=index_id, name=index_name_upper, link=index_link, macro=topic
        )
        if created:
            print(f"Создан индекс: {index_name}")
        else:
            print(f"Индекс уже существует: {index_name}")


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        #EconomicIndex.objects.all().delete()
        #Topic.objects.all().delete()
        populate_data()
        content_names = EconomicIndex.objects.select_related('macro').all()
        print(content_names)
        serializer = EconomicIndexSerializer(content_names, many=True)
        
    return Response(serializer.data)

@api_view(['GET'])
def get_topics(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        #print(content_names)
        serializer = TopicSerializer(topics, many=True)
        
    return Response(serializer.data)

@api_view(['POST'])
def get_economic_indices(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            macro_id = data.get('id')
            print(macro_id)
            if macro_id is not None:
                try:
                    macro = Topic.objects.get(id=macro_id)
                    related_indices = EconomicIndex.objects.filter(macro=macro)
                    serializer = EconomicIndexSerializer(related_indices, many=True)
                    return Response(serializer.data)
                except Topic.DoesNotExist:
                    return JsonResponse({"error": "Macro with the specified ID does not exist."}, status=404)
            else:
                return JsonResponse({"error": "Macro ID parameter is missing."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in the request body."}, status=400)
    
    return JsonResponse({"error": "Invalid request method."}, status=405)

@api_view(['GET'])
def get_economic_index(request):
    if request.method == 'GET':
        EconomicIndex.objects.all().delete()
        Topic.objects.all().delete()
        populate_data()
        content_names = EconomicIndex.objects.select_related('macro').all()
        #print(content_names)
        serializer = EconomicIndexSerializer(content_names, many=True)
        
    return Response(serializer.data)
    