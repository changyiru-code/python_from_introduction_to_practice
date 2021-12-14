cities = {
    'shanxi': {'poulation': 3455, 'country': 'China', 'fact': '煤炭'},
    'shandong': {'population': 7649, 'country': 'China', 'fact': '烧鸡'},
    'sichuan': {'population': 5789, 'coutry': 'China', 'fact': '火锅'},
    }
for city, info in cities.items():
    print(f"城市 {city} 的相关信息如下：")
    for key, value in info.items():
        print('\t'+key+":", value)