import pygame   
import time     # time module ,mins,secs,date, time
import random   # random module means the snake eating food and become bigger,
                  # the food is seleted in random place.

pygame.init()     # initiliaze the game

white = (255,255,255)
yellow =(255,255,102)
black = (0,0,0)
red =   (213,50,80)
green= (0,255,0)
blue =  (50,153,213)

#display size  
dis_width = 600
dis_height =400


dis =pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('HARSHA')
clock = pygame.time.Clock()    

snake_block = 10  #size of snake
snake_speed = 15  #speed of snake

font_style = pygame.font.SysFont("impact",25)     #snakeblock colour  ,fontstyle
score_font = pygame.font.SysFont("impact",20)     # scorefont,fontstyle

def your_score(score):
    value = score_font.render("score:" + str(score),True,black)  #displaying the score on the screen
    dis.blit(value,[0,0])       #blit function is used to create the changes ,dis means display
    

def our_snake(snake_block,snake_list):      #snakeblock and snakelist are arguments
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])   #rectangle,display,colour,xaxis 

def message(mesg,color):      #message passsing after is snake got out
    mesg = font_style.render(mesg,True,color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])   #location,when the game lost the message location
    
def gameLoop():
    game_over =False
    game_close = False
    
    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0
    
    snake_list = []
    Length_of_snake = 1
    #this statement will generate food random
    foodx = round(random.randrange(0, dis_width - snake_block) /10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) /10.0) * 10.0
    
    while not game_over:
        
        
        while game_close== True:   #when the game closes the condition follows 
            dis.fill(blue)
            lost=" You lost press C to play again or Q to Quit"
            message(lost,red)
            your_score(Length_of_snake -1)
            pygame.display.update()
#conditions for either run or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:    #it is based upon the keyright,keyleft,keydown
                    if event.key  == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:     #c means start,q means quit 
                        gameLoop()                  #again loop started
                        
      #changing of keys                  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                
        if x1>= dis_width or x1 <0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change          #+1 snake changes increases
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
        snake_Head =[]
        snake_Head.append(x1) # increasing the snake of xaxis
        snake_Head.append(y1) # increasing the snake of yaxis
        snake_list.append(snake_Head)
        if len(snake_list)  > Length_of_snake:     #if snakelist >length delete one
            del snake_list[0]
        for x in snake_list[:-1]:  #one is removed
            if x == snake_Head:
                game_close = True
                                          
        our_snake(snake_block,snake_list)
        your_score(Length_of_snake - 1)       
            
        pygame.display.update()
        
        # the snake length is developed in this function
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block)/10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block)/10.0) * 10.0
            Length_of_snake +=1
            
        clock.tick(snake_speed)    
       
    pygame.quit()
    quit()
gameLoop() 
            