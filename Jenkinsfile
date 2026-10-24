pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['regression', 'e2e'],
            description: 'Choose the test suite to run in this Jenkins job.'
        )
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox', 'webkit', 'edge'],
            description: 'Choose the browser engine for the test run.'
        )
        booleanParam(
            name: 'HEADLESS',
            defaultValue: false,
            description: 'Run the browser in headless mode when enabled.'
        )
        string(
            name: 'PYTHON_CMD',
            defaultValue: 'python',
            description: 'Python command to use in the CI workspace.'
        )
    }

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
        ALLURE_RESULTS = 'allure-results'
        HEADLESS_OPTION = "${params.HEADLESS ? '--no-headed' : ''}"
        PLAYWRIGHT_BROWSER = "${params.BROWSER == 'chrome' ? 'chromium' : (params.BROWSER == 'edge' ? 'msedge' : params.BROWSER)}"
    }

    stages {
        stage('Create virtual environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv .venv
                            . .venv/bin/activate
                            python -m pip install --retries 5 --timeout 60 -r requirements.txt
                            python -m playwright install $PLAYWRIGHT_BROWSER
                        '''
                    } else {
                        bat '''
                            python -m venv .venv
                            call .\\.venv\\Scripts\\activate.bat
                            python -m pip install --retries 5 --timeout 60 -r requirements.txt
                            python -m playwright install %PLAYWRIGHT_BROWSER%
                        '''
                    }
                }
            }
        }

        stage('Run regression tests') {
            when {
                expression { return params.TEST_SUITE == 'regression' }
            }
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . .venv/bin/activate
                            python -m pytest testcases -m regression --my-browser $BROWSER $HEADLESS_OPTION --alluredir=allure-results --clean-alluredir -v -s
                        '''
                    } else {
                        bat '''
                            call .\\.venv\\Scripts\\activate.bat
                            python -m pytest testcases -m regression --my-browser %BROWSER% %HEADLESS_OPTION% --alluredir=allure-results --clean-alluredir -v -s
                        '''
                    }
                }
            }
        }

        stage('Run E2E test') {
            when {
                expression { return params.TEST_SUITE == 'e2e' }
            }
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . .venv/bin/activate
                            python -m pytest testcases/e2e/Test_EndToEnd.py --my-browser $BROWSER $HEADLESS_OPTION --alluredir=allure-results --clean-alluredir -v -s
                        '''
                    } else {
                        bat '''
                            call .\\.venv\\Scripts\\activate.bat
                            python -m pytest testcases/e2e/Test_EndToEnd.py --my-browser %BROWSER% %HEADLESS_OPTION% --alluredir=allure-results --clean-alluredir -v -s
                        '''
                    }
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                script {
                    allure includeProperties: false,
                        jdk: '',
                        results: [[path: 'allure-results']]
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Pipeline finished. Cleaning workspace artifacts if needed.'
            }
        }
        failure {
            script {
                echo 'The selected suite failed. Review the pytest and Allure output.'
            }
        }
    }
}