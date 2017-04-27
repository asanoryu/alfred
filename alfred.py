# -*- coding: utf-8 -*-

import modules.vocabulary as vc
import modules.searcher as sc
import random
import sys
import modules.speech as sp
import modules.wolfram as wolf_a

context = {'past_searches' :[],
           'name' : [],
            'last_command' : ''       
           }

while True:
        if sys.argv[1] == 'audio':
            userInput = sp.speech_recog()
            if not userInput:
                vc.print_error('Cannot get audio! Falling back to writing')
                userInput = raw_input("text>>> ")
            else:
                vc.print_debug('Got user input: %s' % userInput)
        elif sys.argv[1] == 'text':
            userInput = raw_input("text>>> ")
        else:
            vc.print_error('Unknow arg!')
        userWords = userInput.lower().split(' ')       
        
        
        if vc.word_check(userWords, vc.commands['greetings']):
            if context['last_command'] == 'greeting':
                vc.print_alfred(random.choice(vc.already_did))
                continue
#            print colored('<debug>got greeting', 'blue')
            context['last_command'] = 'greeting'
            vc.print_alfred(random.choice(vc.responses['greetings']))
            
        elif vc.word_check(userWords, vc.commands['farewells']):
#            print colored('<debug>got farewell','blue')
            vc.print_alfred(random.choice(vc.responses['farewells']))
            sys.exit(0)
            
        elif vc.word_check(userWords, vc.commands['courtesy']):
            if context['last_command'] == 'courtesy':
                vc.print_alfred(random.choice(vc.already_did))
                continue
#            print colored('<debug>got greeting', 'blue')
            context['last_command'] = 'courtesy'
#            print colored('<debug>got courtesy','blue')
            vc.print_alfred(random.choice(vc.responses['courtesy']))
            
        elif vc.word_check(userWords, vc.commands['joke']):
            if context['last_command'] == 'joke':
                vc.print_alfred(random.choice(vc.already_did))
                continue
#            print colored('<debug>got greeting', 'blue')
            context['last_command'] = 'joke'
            vc.print_alfred(random.choice(vc.responses['joke']))
            
        elif vc.word_check(userWords, vc.commands['wolfram']):
            search_q = vc.get_search_q(userWords,True)
            if search_q in context['past_searches']:
                vc.print_alfred(random.choice(vc.already_did))
                continue
            context['past_searches'].append(search_q)
            #vc.print_debug('search is: %s' % search_q)
            vc.print_alfred(random.choice(vc.startworking))
            res = wolf_a.get_wolfram_alpha(search_q)
#            vc.print_alfred(random.choice(vc.workdone))
#            vc.print_alfred(next(res).text)

        elif vc.word_check(userWords, vc.commands['search']):
            search_q = vc.get_search_q(userWords)
            if search_q in context['past_searches']:
                vc.print_alfred(random.choice(vc.already_did))
                continue
            context['past_searches'].append(search_q)            

            vc.print_alfred(random.choice(vc.startworking))
            
#            print '<debug> search term is %s' % search_q
            res = sc.google_scrape(search_q)
            related = sc.ddg_rel_search(search_q)
            vc.print_alfred(random.choice(vc.workdone))
            sc.google_pretty_print(res)
            raw_input('press enter to continue...')
            sc.ddg_pretty_print(related)
            
        elif vc.word_check(userWords,(vc.commands['thanks'])):
            vc.print_alfred(random.choice(vc.responses['thanks']))
        else:
            
           vc.print_alfred(random.choice(vc.excuses))
