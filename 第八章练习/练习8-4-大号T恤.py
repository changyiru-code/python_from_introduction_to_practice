def make_shirt(size="L", ziyang="I love python"):
    print(f"该T恤的尺码是{size}, 字样是{ziyang}")
make_shirt()

make_shirt('M')
make_shirt(size='M')

make_shirt('M', 'China')
make_shirt(size='M', ziyang='China')
make_shirt(ziyang='China', size='M')

make_shirt(ziyang='China')

