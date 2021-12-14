# favorite_places = {
#     'zhangsan': ['shanxi', 'zhejiang'],
#     'lisi': ['hainan', 'shandong', 'liaoning'],
#     'wangwu': ['guangzhou'],
#     }
# for name, place in favorite_places.items():
#     if len(place) == 1:
#         print(f"{name} says: my favorite place is {place[0]}", end='')
#         print('.')
#
#     else:
#         print(f"{name} says: my favorite places are", ','.join(place), end='')
#         print('.')

favorite_places = {
    'sam': ['nowyork', 'london', 'paris'],
    'jack': ['beijing', 'tokyo'],
    'rose': ['ottawa'],
}
for name, places in favorite_places.items():
    print('\n' + name.title() + "'s favorit place is:")
    for place in places:
        print('\t' + place.title())
