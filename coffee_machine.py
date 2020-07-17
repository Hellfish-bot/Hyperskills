class Machine:
    
    def __init__(self):
        self.selection = ''
        self.water = 500
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        
    def power(self):
        
        while True:
            self.initial_display()
            if self.selection == 'buy':
                self.buy_display()
            elif self.selection == 'fill':
                self.fill_display()
            elif self.selection == 'take':
                self.take_display()
            elif self.selection == 'remaining':
                self.remaining_display()
            elif self.selection == 'exit':
                break
            
    def buy_display(self):
        
        print('')
        self.selection = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        
        if self.selection == '1':
            
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.milk < 0:
                print('Sorry, not enough milk!')
            elif self.beans < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
    
        if self.selection == '2':
            
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.beans < 20:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -=20
                self.money += 7
                self.cups -= 1
    
        if self.selection == '3':
            
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.beans < 12:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
            
        if self.selection == 'back':
            
            return
    
    def fill_display(self):
        
        print('')
        self.selection = input('Write how many ml of water do you want to add:')
        self.water += int(self.selection)
        self.selection = input('Write how many ml of milk do you want to add:')
        self.milk += int(self.selection)
        self.selection = input('Write how many grams of coffee beans do you want to add:')
        self.beans += int(self.selection)
        self.selection = input('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(self.selection)
        print('')
        
    def take_display(self):
        
        print('')
        print('I gave you $' + str(self.money))
        print('')
        self.money -= self.money
    
    def remaining_display(self):
        
        print('')
        print('The coffee machine has:')
        print(str(self.water) + ' ' + 'of water')
        print(str(self.milk) + ' ' + 'of milk')
        print(str(self.beans) + ' ' + 'of coffee beans')
        print(str(self.cups) + ' ' + 'of disposable cups')
        print('$'+str(self.money) + ' ' + 'of money')
        print('')
        
    def initial_display(self):
        
        self.selection = input('Write action (buy, fill, take, remaining, exit):')
        
machine_test = Machine()
machine_test.power()
