# uptman
`uptman` - пакетный менеджер, можно сказать свой AUR.\
`uptman` - просто оболочка, а `upt` - сам менеджер.\
`upt` - ultimate packaging tool, *но в итоге нифига не ultimate,
просто пародия на* `apt`.\
Этот менеджер скачивает пакеты с GitHub, но поддерживает *зависимости*.\
**Итак, как пользоваться:**\
Основная команда установки:
```
./uptman.py install levm370/PonOS
```
`install` - операция установки\
`levm370/PonOS` - GitHub репозиторий. Можно любой. Эт типа https://github.com/levm370/PonOS.
Так же есть пасхалки:\
`./uptman.py meow meow` - аналог `apt moo moo`.\
В этом менеджере уже есть все пакеты, находящиеся в данный момент на GitHub.\
**Как добавлять зависимости**:
Под словом 'зависимость' здесь подразумевается второй пакет, который нужен основному для работы.\
Для добавления зависимостей в репозиторий нужно создать файл `requirements.txt` и вписать туда зависимости в таком формате:
```
levm370/uptman
levm370/ponos
...
```
Они установятся автоматически./
*P.S. Это самое длинное README которое я писал когда-либо*
