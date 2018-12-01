# API Doc for Spotilyze-Backend

**Authors:** Grant Lee & Richard Yoon

Structure of the System:

```bash
A. API that communicates to Spotify API: backend-api.py
B. API that the iOS client communicates with: frontend-api.py
```

---

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

* **Endpoint:** `/api/users`
	- **parameters**: none
	- **headers**: none
	- **description**: returns all users in Spotilyze's database

* **Endpoint:** `/api/<int:spotify_id>/data/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns all information in database about 
	  specified user by spotify_id

* **Endpoint:** `/api/<int:spotify_id>/data/user_profile/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns user profile of specified
 	  user by spotify_id

* **Endpoint:** `/api/<int:spotify_id>/data/user_playlists/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns playlists followed by specified
	  user by spotify_id

* **Endpoint:** `/api/<int:spotify_id>/data/top_artists_long/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns specified user by spotify_id's
	  top artists over the timespan of **several years**

* **Endpoint:** `/api/<int:spotify_id>/data/top_artists_mid/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns specified user by spotify_id's
	  top artists over the timespan of the past **6 months**

* **Endpoint:** `/api/<int:spotify_id>/data/top_artists_short/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns specified user by spotify_id's
	  top artists over the timespan of the past **4 weeks**

* **Endpoint:** `/api/<int:spotify_id>/data/top_tracks_long/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns specified user by spotify_id's
	  top tracks over the timespan of **several years**

* **Endpoint:** `/api/<int:spotify_id>/data/top_tracks_mid/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns specified user by spotify_id's
	  top tracks over the timespan of the past **6 months**

* **Endpoint:** `/api/<int:spotify_id>/data/top_tracks_short/`
	- **parameters**: spotify_id
	- **headers**: none
	- **description**: returns specified user by spotify_id's
	  top tracks over the timespan of the past **4 weeks**
