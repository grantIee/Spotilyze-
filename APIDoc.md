# API Doc for Spotilyze-Backend

**Authors:** Grant Lee & Richard Yoon

Structure of the System:

```bash
A. API that communicates to Spotify API: backend-api.py
B. API that the iOS client communicates with: frontend-api.py
```

### `backend-api.py` documentation:
*This api handles authentication of the user and retrieves and stores
relevant information from the user from Spotify*

* **Endpoint:** `/`
	- **parameters**: none
	- **headers**: client_id
	- **description**: specifies the redirect_uri and scopes

* **Endpoint:** `/callback/q`
	- **parameters**: none
	- **headers**: authentication information 
	- **description**: after receiving the token, this endpoint will 
 	  retrieve the relevant information from Spotify. 


### `frontend-api.py` documentation:
*This api provides the front-end client with the necessary requests 
from the compiled database from the backend api*

* **Endpoint:** `/`
	- **parameters**: none
	- **headers**: client_id
	- **description**: specifies the redirect_uri and scopes

* **Endpoint:** `/callback/q`
	- **parameters**: none
	- **headers**: authentication information 
	- **description**: after receiving the token, this endpoint will 
 	  retrieve the relevant information from Spotify. 
