# Nero_autotests

<<<<<<< HEAD
Перед запуском теста из командной строки Windows или терминала PyCharm необходимо активировать виртуальное окружение: 
		
		...\Nero_autotests\venv\nero_emvironment\Scripts>activate.bat 

Для запуска тестов необходимо, находясь в корневом каталоге проекта, выполнить следующую команду: 	
		
		pytest -s -v --tb=line tests
		
при этом будут выполнены все тестовые методы во всех имеющихся файлах тестов test_ТЕСТИРУЕМЫЙ_ОБЪЕКТ.py

Браузер по умолчанию - Google Chrome, но, также предусмотрена возможность запуска тстов в браузере Mazila Firefox.
Предполагается, что драйвер браузера установлен и для запуска необходимо указать параметра запуска браузера в команде 
запуска тестов:
        
        pytest -s -v --browser_name=firefox --tb=line tests
        
По умолчанию язык запуска интерфейса приложения - русский, но, используя параметр запуска, можно выбрать язык запуска
английский:

        pytest -s -v --browser_name=firefox --language=en --tb=line tests
        
Если нет необходимости выполнять все тесты из папи test, необходимо, находясь в дериктории с тестами выполнить 
следующую команду:

        pytest -s -v --tb=line test_ТЕСТИРУЕМЫЙ_ОБЪЕКТ.py
        
                


=======
