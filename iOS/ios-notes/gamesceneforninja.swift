//
//  GameScene.swift
//  NinjaAimTest
//
//  Created by Jennifer Zeller on 9/9/16.
//  Copyright (c) 2016 Alex. All rights reserved.
//

import SpriteKit
import CoreMotion

class GameScene: SKScene {
    
    var crosshair = SKSpriteNode()
    var motionManager = CMMotionManager()
    
    // for gravity: DISABLED CURRENTLY
    var destX:CGFloat = 0.0
    
    override func didMoveToView(view: SKView) {
        physicsWorld.gravity = CGVector(dx: 0, dy: 0)
        /* Setup your scene here */
        if motionManager.accelerometerAvailable {
            motionManager.accelerometerUpdateInterval = 0.1
            motionManager.startAccelerometerUpdates()
            motionManager.startAccelerometerUpdatesToQueue(NSOperationQueue.mainQueue()){
                (data, error) in
                
                let currentX = self.crosshair.position.x
                
                if data!.acceleration.x < 0 {
                    self.destX = currentX + CGFloat(data!.acceleration.x * 1000)
                }
                    
                else if data!.acceleration.x > 0 {
                    self.destX = currentX + CGFloat(data!.acceleration.x * 1000)
                }
            }
            let action = SKAction.moveToX(self.destX, duration: 0.5)
            self.crosshair.runAction(action)

            // motionManager.startGyroUpdates()
            //let queue = NSOperationQueue.mainQueue()
            // motionManager.startGyroUpdatesToQueue(queue) {
                //(data, error) in
                // change crosshair.position
                // }
            }
        
        // for gravity
        // self.physicsWorld.gravity = CGVectorMake(0.0, -9.8)
        // crosshair
        let crosshair = SKSpriteNode(imageNamed: "crosshairs")
        crosshair.position = CGPointMake(frame.midX, frame.midY)
        
        // for gravity
        crosshair.physicsBody = SKPhysicsBody(circleOfRadius: 10)
        crosshair.physicsBody!.linearDamping = 0.5
        // crosshair.physicsBody!.dynamic = true;
        // crosshair.physicsBody!.affectedByGravity = true;
        
        self.addChild(crosshair)
        
        // for gravity
//        if motionManager.accelerometerAvailable == true {
//            motionManager.startAccelerometerUpdatesToQueue(NSOperationQueue.currentQueue()!, withHandler:{
//                data, error in
//                let currentX = self.crosshair.position.x
//                if data!.acceleration.x < 0 {
//                    self.destX = currentX + CGFloat(data!.acceleration.x * 100)
//                }
//                else if data!.acceleration.x > 0 {
//                    self.destX = currentX + CGFloat(data!.acceleration.x * 100)
//                }
//            })
//        }
        
        // Timer for Targets
        _ = NSTimer.scheduledTimerWithTimeInterval(3.0, target: self, selector: #selector(GameScene.spawnTargets), userInfo: nil, repeats: true)
        
        
    }
    
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
       /* Called when a touch begins */
        
        for touch in touches {
            let location = touch.locationInNode(self)
            
            let shape = SKShapeNode(circleOfRadius: 10)
            shape.strokeColor = SKColor.blackColor()
            shape.fillColor = SKColor.greenColor()
            shape.xScale = 0.5
            shape.yScale = 0.5
            shape.position = location // crosshair.position
            
            //            let action = SKAction.rotateByAngle(CGFloat(M_PI), duration:1)
            
            //            sprite.runAction(SKAction.repeatActionForever(action))
            
            self.addChild(shape)
        }
    }
   
    override func update(currentTime: CFTimeInterval) {
        /* Called before each frame is rendered */
        
        // for gravity
//        var action = SKAction.moveToX(destX, duration: 1)
//        self.crosshair.runAction(action)

    }

    // creates the targets... we should replace this to be faster
    func spawnTargets(){
        let OuterRing = SKShapeNode(circleOfRadius: 110 )
        OuterRing.zPosition = -1.0
        OuterRing.strokeColor = SKColor.blackColor()
        OuterRing.glowWidth = 1.0
        OuterRing.fillColor = SKColor.whiteColor()
        
        let OuterRing2 = SKShapeNode(circleOfRadius: 90 )
        OuterRing2.zPosition = -1.0
        OuterRing2.strokeColor = SKColor.whiteColor()
        OuterRing2.glowWidth = 1.0
        OuterRing2.fillColor = SKColor.blackColor()
        
        let MiddleRing = SKShapeNode(circleOfRadius: 70 )
        MiddleRing.zPosition = -1.0
        MiddleRing.strokeColor = SKColor.blackColor()
        MiddleRing.glowWidth = 1.0
        MiddleRing.fillColor = SKColor.blueColor()
        
        let InnerRing = SKShapeNode(circleOfRadius: 50 )
        InnerRing.zPosition = -1.0
        InnerRing.strokeColor = SKColor.blackColor()
        InnerRing.glowWidth = 1.0
        InnerRing.fillColor = SKColor.redColor()
        
        let BullsEye = SKShapeNode(circleOfRadius: 30 )
        BullsEye.zPosition = -1.0
        BullsEye.strokeColor = SKColor.blackColor()
        BullsEye.glowWidth = 1.0
        BullsEye.fillColor = SKColor.yellowColor()
        
        let MinValue = self.size.width/6
        let MaxValue = self.size.width-10
        let SpawnPoint = UInt32(MaxValue-MinValue)
        let random_start = arc4random_uniform(SpawnPoint)
        OuterRing.position = CGPoint(x: CGFloat(random_start), y: self.size.height)
        OuterRing2.position = CGPoint(x: CGFloat(random_start), y: self.size.height)
        MiddleRing.position = CGPoint(x: CGFloat(random_start), y: self.size.height)
        InnerRing.position = CGPoint(x: CGFloat(random_start), y: self.size.height)
        BullsEye.position = CGPoint(x: CGFloat(random_start), y: self.size.height)
        self.addChild(OuterRing)
        self.addChild(OuterRing2)
        self.addChild(MiddleRing)
        self.addChild(InnerRing)
        self.addChild(BullsEye)
        let action = SKAction.moveToY(-130, duration: 7.0)
        OuterRing.runAction(SKAction.repeatActionForever(action))
        OuterRing2.runAction(SKAction.repeatActionForever(action))
        MiddleRing.runAction(SKAction.repeatActionForever(action))
        InnerRing.runAction(SKAction.repeatActionForever(action))
        BullsEye.runAction(SKAction.repeatActionForever(action))
    }
    
}
