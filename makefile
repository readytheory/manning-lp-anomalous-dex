run:
	docker run -d -p 7777:7777 -v /c/py/liveproj/jupyter/notebooks:/notebooks   -v /c/py/liveproj/jupyter/data:/data  levin/lp-service
