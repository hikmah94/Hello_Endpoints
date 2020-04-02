
/**
 * After the client library has loaded, this init() function is called.
 * The init() function loads the helloworldendpoints API.
 */

function init() {
	
	// You need to pass the root path when you load your API
	// otherwise calls to execute the API run into a problem
	
	// rootpath will evaulate to any of these, depending on where the app is running:
	// //for running locally in your matchine
	// //localhost:8080/_ah/api
	// // for already deployed application
	// //your-app-id/_ah/api

	var rootpath = "//" + window.location.host + "/_ah/api";
	
	// Load the helloworldendpoints API
	// If loading completes successfully, it will call loadCallback function
	gapi.client.load('helloworldendpoints', 'v1', loadCallback, rootpath);
}



