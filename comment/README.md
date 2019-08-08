##08/08 总结
1. redirect()重定向问题，如果接受的参数为模型的话，则需要在模型中就实现get_absolute_url，否则会报错
2. 待解决的问题，不知道为什么在Comment中加一个属性author，外键到User会报错，目前无解
3. form的前端操作目前不是很了解，只是装上了轮子，TODO
4. 对前后端的映射关系还不是很清晰，对'namespace:name'和'xx/xx.html'理解不深，导致会有混淆
