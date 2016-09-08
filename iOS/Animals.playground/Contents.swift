class Animal{
    var name: String
    var health = 100
    init(name: String){
        self.name = name
    }
    func displayHealth()->Animal{
        print(self.health)
        return self
    }
}

class Cat: Animal{
    //var something: String
    override init(name: String){
        //self.something = something
        super.init(name: name)
        self.health = 150
    }
    func growl()->Cat{
        print("RAWR!")
        return self
    }
    func run()->Cat{
        if self.health < 10{
            print("Not enough health to run")
        } else{
            print("Running")
            self.health-=10
        }
        return self
    }
    override func displayHealth()->Cat{
        print(self.health)
        return self
    }
}

class Lion: Cat{
    override init(name: String){
        super.init(name: name)
        self.health = 200
    }
    override func growl()->Lion{
        print("ROAR! I AM KING OF THE JUNGLE")
        return self
    }
    override func run()->Lion{
        print("Running")
        self.health-=10
        return self
    }
    override func displayHealth()->Lion{
        print(self.health)
        return self
    }
}

class Cheetah: Cat{
    override init(name: String){
        super.init(name: name)
        self.health = 200
    }
    override func run()->Cheetah{
        if self.health < 50{
            print("Not enough health to run")
        } else{
            print("Running Fast")
            self.health-=50
        }
        return self
    }
    override func displayHealth()->Cheetah{
        print(self.health)
        return self
    }
    func sleep()->Cheetah{
        if self.health > 150{
            self.health=200
        } else {
            self.health+=50
        }
        return self
    }
}

var kitty = Cheetah(name: "kitty")
kitty.run().run().run().run().displayHealth()
var simba = Lion(name:"Simba")
simba.run().run().run().growl()