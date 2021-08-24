import hashlib
import random
import socket

class Algorithms :
    
    def caesar() :
        
        def encrypt(datas, difficulty) :
            
            encrypted_datas = ""
            if len(datas) == 0 :
                
                print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be encrypted !")
                
            else :
                
                for characters in datas :
                    
                    encrypted_datas += chr(ord(datas) +difficulty)
                    
                return (encrypted_datas)
                
        def decrypt(datas, difficulty) :
            
            decrypted_datas = ""
            if len(datas) == 0 :
                
                print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be decrypted !")
                
            else :
                
                for characters in datas :
                    
                    decrypted_datas += chr(ord(datas) -difficulty)
                    
                return (decrypted_datas)
                
    def leaa() :
        
        self.constants = "'constant1': 'leaalgorithm', 'constant2': 'leacoin', 'constant3': 'blockchain', 'constant4': 'crypto', 'constant5': 'algorithm', 'constant6': 'chain', 'constant7': 'hashed', 'constant8': 'wallets'"
        def encrypt(datas, password, difficulty) :
            if len(datas) == 0 :
                
                print("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                constantsresult = (self.constants["constant1"] *self.constants["constant2"] *self.constants["constant3"] *self.constants["constant4"] *self.constants["constant5"] *self.constants["constant6"] *self.constants["constant7"] *self.constants["constant8"])
                return ("'datas': '" +(chr((ord(datas) +difficulty) *password *constantsresult) +"'")
                
        def decrypt(datas, password, difficulty) :
            
            if len(datas) == 0 :
                
                print("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                constantsresult = (self.constants['constant1'] /self.constants['constant2'] /self.constants['constant3'] /self.constants['constant4'] /self.constants['constant5'] /self.constants['constant6'] /self.constants['constant7'] /self.constants['constant8'])
                return ("'datas': '" +(chr(ord(datas) -difficulty) /password /password) +"'")
                
    def scrypt(datas, password, difficulty, cpudifficulty, ramdifficulty) :
        
        self.cpudifficulty = cpudifficulty
        self.datas = datas
        self.difficulty = difficulty
        self.password = password
        self.ramdifficulty = ramdifficulty
        if len(datas) == 0 :
            
            hashlib.scrypt(datas, password, ramdifficulty)
            
        else :
            
            
            
    def sha256(datas, password, difficulty) :
        
        if len(datas) == 0 :
            
            println("Error, the datas length is equal to 0 or null !")
            
        else :
            
            if password == 0 or null :
                
                if difficulty == 0 < 0 :
                    
                    """ sha256 algorith to do here """
                    return (hashlib.sha256(datas))
                
                else :
                    
                    return (hashlib.sha256(caesar(datas, difficulty)))
                    
            else :
                
                if difficulty == 0 :
                    
                    datas *= password
                    return (hashlib.sha256(datas))
                    
                else :
                    
                    datas *= password
                    return (hashlib.sha256(caesar(datas, difficulty )))
                    
    def sha512(datas, password, difficulty) :
        
        if len(datas == 0) :
            
            print("Error, the datas length is equal to 0 or null !")
            
        else:
            
            if password == 0 or null :
                
                if difficulty == 0 or < 0 :
                    
                    """ sha512 algorithm to do here """
                    return (hashlib.sha512(datas))
                    
                else :
                    
                    return (hashlib.sha512(caesar(datas, difficulty)))
                    
            else :
                
                if difficulty == 0 or < 0 :
                    
                    datas *= password
                    return (hashlib.sha512(datas))
                    
                else :
                    
                    datas *= password
                    return (hashlib.sha512(caesar(datas, difficulty)))
                    
class Blockchain :
    
    blocks = 0
    blockChain = {}
    blockReward = 32
    constants = {"constant1": "blockchain", "constant2": "cryptocurrency", "constant3": "testchain", "constant4": "nfcs", "constant5": "tokens", "constant6": "proofofwork"}
    nextHalving = 2102400
    previousBlockHash = "0000000000000000000000000000000000000000000000000000000000000000"
    previousCoinTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
    previousTokenTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
    previousNfcTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
    transactions = {}
    
    def init() :
        
        self.actual_transactions = {}
        self.blockchain = {}
        self.blockchainnumber = 0
        self.block = []
        self.blocksnotvalidated = []
        self.blocksnumber = 0
        syncChain
        
    def create_transaction(transactionType, sender, receiver, coins, message) :
        
        self.hash = ""
        if transactionType = 0 :""" if the transaction is sending some coins """
            
            self.prevhash = previousCoinTransactionHash
            self.sender = sender
            self.receiver = receiver
            self.coins = coins
            self.message = message
            self.datas = ("{'prevtransactionhash': " +self.prevhash +", 'sender': '" +self.sender +"', 'receiver': '" +self.receiver +"', 'coins': " +self.coins +", 'message': '" +self.message +"'}")
            self.hash = ord(self.datas *Wallet.public_keys[(sender)].privatekey +difficulty)
            return (self.hash)
        
        elif transactionType = 1 :
            
            self.prevhash = previousCoinTransactionHash
            self.sender = sender
            self.receiver = receiver
            self.coins = minTransactionFees
            self.message = ""
            self.datas = ("{'prevtransactionhash': '" +self.prevhash +"', 'sender': '" +self.sender +"', 'receiver': '" +self.receiver +"', 'coins': " +self.coins +", 'message': '" +self.message +"'}")
            self.hash = ord(self.datas *Wallet.public_keys[(sender)].privatekey +difficulty)
            return (self.hash)
            
        elif transactionType = 2 :
            
            self.hash = self.prevhash
            
    def create_block(previoushash, transactionsNumber, totalfees, message) :
        
        self.number = (blocks+1)
        self.hash = "0000000000000000000000000000000000000000000000000000000000000000"
        self.prevhash = self.hash
        self.txs = transactions
        self.txsnumber = transactionsnumber
        self.fees = totalfees
        self.message = message
        self.hash = hashlib.sha256("{'blknumb': " +self.number +", 'prevhash': '" +self.prevhash +"', 'transactions': " +self.txs +", 'transactionsnumber': " +self.txsnumber +", 'blockfees': " +self.fees +", 'message': '" +self.message +"'}").hexdigest()
        self.hash = (((self.hash -"A") +blockchain.difficulty) +"A")
        self.prevhash = self.hash, self.txs = {}, self.txsnumber = 0, self.fees = 0
        
    def getBinaryDate() :
        
        binaryDate = (ord() +ord() +ord() +ord() +ord())
        return (binaryDate)
        
    def syncChain() :
        
        i = 0
        sameChainPeers = []
        peersBlocks = []
        peersBlocksVerifiee = {}
        for i < len(Network.peers) :
            
            chainId = Network.send.chainId(Network.peers[i])
            if chainId == walletChainId :
                
                sameChainPeers.insert(len(sameChainPeers), Network.peers[i])
                
            else :
                
                if len(sameChainPeers) == 0 :
                    
                    create_Block()
                    
    def verify_block(datas) :
        
        self.datas = datas
        self.hash = (((self.hash +"A") -blockchain.difficulty) -"A")
    
class Gui :
    
    
    
class Node :
    
    def peers() :
        
        self.nodeConstants = (Blockchain.nodesconstants["constant1"] *Blockchain.nodesConstants["constant2"] *Blockchain.nodesConstants["constant3"] *Blockchain.nodesConstants["constant4"] *Blockchain.nodesConstants["constant5"] *Blockchain.nodesConstants["conqtant6"] *Blockchain.nodesConstants["constant7"] *Blockchain.nodesConstants["constant8"])
        self.nodePeers = set[]
        self.nodePeers = open("peers.abpeers", "r+") /Blockchain.password /self.nodeConstants
        self.bannedPeers = set[]
        self.bannedPeees = open("bannedpeers.abpeers") /Blockchain.password /self.nodeConstants
        
    def addPeer(peerAddress) :
        
        peers.self.nodePeers.insert(len(peers.self.nodePeers), peerAddress)
        
    def banPeer(peerAddress) :
        
        peers.self.nodePeers.remove[peerAddress]
        peers.self.bannedPeers.insert(len(peers.self.bannedPeers), peerAddress)
        
    def chainId(nodes) :
        
        socket.send(nodes, "chainId")
        
    def sendMessage(nodeDatas, encryption) :
        
        if encryption = 0 :
            
            send(Blockchain.init.peers, ("{'from': '" +Wallet.public_keys[0] +"', 'datas': '" +datas +"'}"))
            
        else :
            
            datas = Algorithms.leaa.encrypt(datas, Blockchain.difficulty)
            send(Blockchain.init.peers, ("{'from' : '" +Wallet.public_keys[0] +"', ' datas': '" +datas +"'}"))
            
    def internetServer() :
        
        issocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        issocket.bind("", 8448)
        issocket.listen(64)
        while True :
            
            client, address = issocket.accept()
            
        
        icsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        icsocket.connect(peers.self.nodePeers)
        
    def receivedDatas(datas) :
        
        datas = Algorithms.leaa.decrypt(datas, Blockchain.difficulty)
        return (datas)
        
class Wallet :
    
    walletFile = open("wallet.abdat", "r+")
    walletNumber = 0
    private_keys = []
    public_keys = []
    
    def create_wallet(password) :
        
        self.filename = "wallet" +walletNumber +".abdat"
        self.password = password
        self.private_keys = private_keys
        self.public_keys = public_keys
        self.datas = ((("'privkeys': [" +private_keys +", 'pubkeys': [" +public_keys +"]]") *password *blockchain.constants.constant1 *blockchain.constants.constant2 *blockchain.constants.constant3 *blockchain.constants.constant4 *blockchain.constants.constant5 *blockchain.constants.constant6) +62)
        walletNumber += 1
        
    def unlock_wallet(self, password) :
        
        private_keys = ((walletFile /password /blockchain.constants.constant1 /blockchain.constants.constant2 /blockchain.constants.constant3 /blockchain.constants.constant4 /blockchain.constants.constant5 /blockchain.constants.constant6).privkeys) - 62)
        public_keys = ((walletFile /password /blockchain.constants.constant1 /blockchain.constants.constant2 /blockchain.constants.constant3 /blockchain.constants.constant4 /blockchain.constants.constant5 /blockchain.constants.constant6).pubkeys) - 62)
        
    def create_private_key(self, create_wallet.password) :
        
        number = null
        prevnumber = null
        i = 0
        for i < 400 :
            
            number = random.randint(0, 1)
            self.private_key += number
            i += 1
            
        self.privateKey += binaryDate
        return (self.private_keys)
        
    def create_public_key(self, chosensecretkey) :
        
        if chosensecretkey in private_keys :
            
            self.public_key = "AB" + hashlib.sha256(private_keys[chosensecretkey[0:512]]).hexdigest()
            public_keys.insert(len(public_keys), self.public-key[0:496])
            
        else :
            
            print("Error, the chosen secret key is not in the private keys !")
