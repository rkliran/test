pytest --alluredir report

COPY config\environment.properties report

allure generate report/ -o report/html

allure open allure-report