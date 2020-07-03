## Общая инструкция по развертыванию проекта с Github

1.  Создаем и заходим в << рабочую >> папку, открываем из нее терминал и пишем команду скачивания проекта:  
    * ***```git clone https://github.com/Klastoor/XXXXXXXX```*** где вместо **ХХХХ** вписываем название проекта напр: 
    ***```Site_shop```***
    *   После этого в папке появится новая папка с названием проекта, переходим в нее - теперь эта папка **<< рабочая >>**
    *   Для перехода терминала (что бы он работал из под этой папки) 
    ***```cd XXXX```*** где **XXXX** название скаченного проекта(соблюдая регистр!) напр 
    ***```cd Site_shop```***

* * *

2.  Теперь в рабочей папке мы создаем виртуальное окружение и в ней будем работать! команда - ***```virtualenv venv```***
    *   После команды в папке с проектом появится новая папка **venv** в неё не надо переходить, просто для информации и индикатор того что все создалось

* * *

3.  Создав виртуальное окружение, необходимо его активировать, в каждой ос это разные команды, но вот в линуксе например 
***```source venv/bin/activate```***
    *   При успешной активации теперь в терминале, в строке ввода команд - появится надпись **(venv)**

* * *

4.  Теперь,из за того что, это только что - отдельно созданая среда, необходимо снова установить **pip пакеты** напр: (
***```pip3 install flask```***), но что бы не вписывать все это вручную, чаще всего в скаченном git проекте имеется файлик **requirements.txt** и в нем уже записаны все необходимые пакеты, что бы активировать его следует написать 
***```pip install -r requirements.txt```***

* * *

5.  Осталось только запустить проект набрав команду 
***```./run.py```*** или 
***```python3 run.py```*** (после запуска команды, ввод других команд невозможен)
    *   После запуска команды, должно появится сообщение похожее на это `Running on http://127.0.0.1:4567/ (Press CTRL+C to quit)` в котором говорится что просмотр сайта происходит по вот этой ссылке `http://127.0.0.1:4567` а что бы закрыть приложение нажмите *CTRL+C*

* * *

<span>**P.S** иногда в терминале есть фишка автозаполнения, если к примеру ввести первую букву команды и нажать на **Tab** то зачастую он дописывает все слово</span>

<span>**P.SS** для редактирования странички, после запуска приложения следует в каком либо текстовом редакторе открыть нужную страничку, все странички лежат в **рабочая папка > app > templates > ..все странички..**</span>

<span>**P.SSS** данная инструкции подходит лишь в том случае - если на компьютере еще нет папки с проектом</span>
