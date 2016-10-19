// angular routes

var app = angular.module('app', ['ngRoute']);
app.config(function ($routeProvider) {
  $routeProvider
  // load partial for root route
    .when('/', {
      templateUrl: '/partials/index.html',
      controller: 'indexController'
    })
    // http://localhost:8000/#/
    .when('/edit/:id', {
      templateUrl: '/partials/edit.html',
      controller: 'indexController',
    })
    // http://localhost:8000/#/new
    .when('/new', {
      templateUrl: '/partials/new.html',
      controller: 'newController',
    })
    // http://localhost:8000/#/show/
    .when('/show/:id', {
      templateUrl: '/partials/show.html',
      controller: 'indexController',
    })
    // run delete from index controller
    .when('/friends/:id/destroy', {
      controller: 'indexController',
    })
    .otherwise({
      redirectTo: '/'
    });
});
