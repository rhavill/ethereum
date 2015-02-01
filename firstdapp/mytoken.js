//var contractAddress = '0x5a5b7c82bbeb7f871f92d98bb93279c98a7f1abb';
var contractAddress = '0x37f87a88443fb57f130868ad966094d8c6f886d6';

function createTransaction() {
	var receiverAddress = '0x' + document.querySelector('#receiverAddress').value;
	var amount = document.querySelector('#amount').value;
	var data = [receiverAddress, amount];
	web3.eth.transact({to: contractAddress, data: data, gas: 5000});
}

// web3.eth.watch({altered: {at: web3.eth.accounts[0], id: contractAddress}}).changed(function() {
// 	document.getElementById('balance').innerText = web3.toDecimal(web3.eth.stateAt(contractAddress, web3.eth.accounts[0]));
// });

web3.eth.watch().changed(function(){
  web3.eth.storageAt(contractAddress).then(function(result) {
  	document.getElementById('balance').innerText = web3.toDecimal(result["0x39063fd6ac20a84420d61b2d3c556ae25c258419"]);
  	console.log(result);
  });
}); 
