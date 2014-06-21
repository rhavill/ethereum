#!/usr/bin/python

import serpent
from pyethereum import transactions, blocks, processblock, utils

# Compile serpent code in namecoin.se file.
code = serpent.compile(open('namecoin.se').read())
# Create a private key based on the password "password".
key = utils.sha3('cow')

# Create an address from the private key.
addr = utils.privtoaddr(key)
print 'Addr is ' + addr

# # Create a genesis block and assign 1018 wei (1 ether) to my address.
genesis = blocks.genesis({ addr: 10**18 })

# # Create and sign a contract transaction.
# # def contract(nonce, gasprice, startgas, endowment, code, v=0, r=0, s=0):
tx1 = transactions.contract(0,10**12,10000,0,code).sign(key)

# # Apply the contract transaction.
result, contract = processblock.apply_transaction(genesis,tx1)
print 'Contract creation result is ' + str(result) + ' Contract address is ' + contract

# # Send a new transaction to the existing contract to register "george" to 45 after packging the data.
tx2 = transactions.Transaction(1,10**12,10000,contract,0,serpent.encode_datalist(['george',45])).sign(key)

# # Apply the new transaction.
result, ans = processblock.apply_transaction(genesis,tx2)
print 'Registration result is ' + str(result) + ' Answer is ' + str(serpent.decode_datalist(ans))

print 'Genesis ' + str(genesis.to_dict())
# # 'nonce': '\x04\x99Og\xdcU\xb0\x9e\x81J\xb7\xff\xc8\xdf6\x86\xb4\xaf\xb2\xbbS\xe6\x0e\xae\x97\xef\x04?\xe0?\xb8)', 'min_gas_price': 1000000000000000L, 'extra_data': '', 'state_root': '', 'difficulty': 4194304, 'timestamp': 0, 'number': 0, 'gas_used': 2712L, 'coinbase': '0000000000000000000000000000000000000000', 'tx_list_root': '\x17\x90\x87\x966\xbdb!\x14|R\xb0& \xb04\x90\xb9bs\x12\x85\x90\xdaB\xed\x83n*\x8eE\x8e', 'state': {'0000000000000000000000000000000000000000': {'nonce': 0L, 'balance': 2712000000000000L, 'storage': {}, 'code': ''}, 'da7ce79725418f4f6e13bf5f520c89cec5f6a974': {'nonce': 0L, 'balance': 0L, 'storage': {113685359126373L: 45L}, 'code': '60003556601e596020356000355760015b525b54602052f260285860005b525b54602052f2'}, 'cd2a3d9f938e13cd947ec05abc7fe734df8dd826': {'nonce': 2L, 'balance': 997288000000000000L, 'storage': {}, 'code': ''}}, 'uncles_hash': '\x1d\xccM\xe8\xde\xc7]z\xab\x85\xb5g\xb6\xcc\xd4\x1a\xd3\x12E\x1b\x94\x8at\x13\xf0\xa1B\xfd@\xd4\x93G', 'prevhash': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 'gas_limit': 1000000}
print 'Balance ' + str(genesis.get_balance(addr))
# # 997288000000000000L
storage_data = genesis.get_storage_data(contract,'george')
print 'Storage data ' + str(storage_data)