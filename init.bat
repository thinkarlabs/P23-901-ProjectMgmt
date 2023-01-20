@ECHO OFF
if not exist "penv" (
	py -m venv penv
) 

.\penv\Scripts\activate