(function(){

var app = angular.module('store', []);

var app = angular.module('MyApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('StoreController', function(){
	this.products = gems;


});

app.controller('PanelController', function(){
	this.tab=1; // initialize tab in controller instead of ng-init
	this.reviews = reviews;
	
	this.selectTab= function(setTab){
		this.tab = setTab;
	};

	this.isSelected=function(checkTab){
		return this.tab === checkTab;
	}

});

app.controller("ReviewController", function(){ 
	this.review ={};

	this.addReview = function(product){
		// console.log(product);
		product.reviews.push(this.review);
		this.review = {};
	}
})

var gems = [
	{
		name: 'Dodecahedron',
		price: 2.95,
		description: 'a nice gem',
		canPurchase: false,
		soldOut: true,
		images: [
			{full:'./assets/img/dec.png',
			thumb:'./assets/img/dec_th.png'},
		],
	},

	{
		name: 'Pentagonal',
		price: 33,
		description: 'a five-sided gem',
		canPurchase: false,
		soldOut: true,
		images: [
			{full:'./assets/img/pent.png',
			thumb:'./assets/img/pent_th.png'},
		],
	},

	{
		name: 'Round',
		price: 17.67,
		description: 'a round gem',
		canPurchase: false,
		soldOut: true,
		images: [
				{full:'./assets/img/round.png',
				thumb:'./assets/img/round_th.png'},
			],
	},
]

var reviews=[
{
	stars:5,
	body: "I love this gem!",
	author: "joe@joe.com",
},
{
	stars:4,
	body: "This is good.",
	author: "jill@egg.com",
},
{
	stars:3,
	body: "This is mediocre.",
	author: "lawrence@egg.com",
},
{
	stars:2,
	body: "This is lame.",
	author: "brody@egg.com",
},
{
	stars:1,
	body: "This sucks.",
	author: "jasmine@egg.com",
},
]

})();
