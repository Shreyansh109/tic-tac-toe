def ttt():
	import time
	import random
	time.sleep(1)
	print('Manan: Hi!')
	print()
	print("Manan: This is Manan \U0001F60A")
	time.sleep(.5)
	print("Manan: I shall assist you to")
	time.sleep(1.7)
	print('play')
	time.sleep(1.6)
	print("Tic")
	time.sleep(.8)
	print("Tac")
	time.sleep(.8)
	print("Toe")
	print()
	time.sleep(1)
	print('Wait')
	time.sleep(.7)
	print('Wait')
	time.sleep(.7)
	print('Wait')
	print()
	print('Hmmm...')
	time.sleep(2)
	print("Manan: Please give me command carefully because if you give wrong command I shall die so please \U0001F97A ")
	print()
	time.sleep(1.4)
	print("Manan: Now,Arrrrre you ready to play...")
	yu=input('You: ')
	if 'you' in yu.lower() and 'not ready' in yu.lower():
		print("Manan: oh come on you think only about you I'm always ready")
		yu=input('You: ')
	if 'y' in yu.lower() or 'ye' in yu.lower() or 'yes' in yu.lower() or 'yup' in yu.lower() or 'ya' in yu.lower() or 'sur' in yu.lower() or 'ready' in yu.lower() or 'start' in yu.lower():
		print('''Manan: I'm also ready\nand exited to play with you''')
		print("Tooo")
		time.sleep(.9)
		print("Manan: ye raha aap ke screen par")
		print()
		print()
		bo=print('''  1   |  2  |  3  
-----------------
  4   |  5  |  6  
-----------------
  7   |  8  |  9''')
		print()
		print("Manan: Now I define some rule to play this")
		print()
		print("Manan: Basicaly you know basic rule so, I will not explain that rule I shall only explain how to fill block")
		time.sleep(.7)
		print("Manan: you got a simble (×/o) you just enter number where you want to put that symbol")
		corc=['x','o']
		print()
		usy=corc[random.randint(0,1)]
		print('Manan: You got',usy)
		bo1r=['  ',1,'   |   ',2,'   |   ',3]
		bo2r=['  ',4,'   |   ',5,'   |   ',6]
		bo3r=['  ',7,'   |   ',8,'   |   ',9]
		bo1is=[1,3,5]
		bo2is=[1,3,5]
		bo3is=[1,3,5]
		bovs=[bo1r,bo2r,bo3r]
		if usy=='o':
			time.sleep(.9)
			print()
			print("Manan: I'm first")
			print()
			print()
			time.sleep(1.2)
			for sg in range(0,4):
				ccr=random.randint(1,len(bovs))
				if bo1r in bovs:
					if ccr-1==bovs.index(bo1r):
						ccp=random.randint(0,len(bo1is)-1)
						ccpf=bo1is[ccp]
						bo1r[ccpf]='×'
						bo1is.remove(ccpf)
						print(bo1is)
						print(bo1r)
						print('-'*40)
						print(bo2r)
						print('-'*40)
						print(bo3r)
						print()
						if bo1r in bovs:
							if len(bo1is)==0:
								bovs.remove(bo1r)
						if bo2r in bovs:
							if len(bo2is)==0:
								bovs.remove(bo2r)
						if bo3r in bovs:
							if len(bo3is)==0:
								bovs.remove(bo3r)
				if bo2r in bovs:
					if ccr-1==bovs.index(bo2r):
						ccp=random.randint(0,len(bo2is)-1)
						ccpf=bo2is[ccp]
						bo2r[ccpf]='×'
						bo2is.remove(ccpf)
						print(bo2is)
						print(bo1r)
						print('-'*40)
						print(bo2r)
						print('-'*40)
						print(bo3r)
						print()
						if bo1r in bovs:
							if len(bo1is)==0:
								bovs.remove(bo1r)
						if bo2r in bovs:
							if len(bo2is)==0:
								bovs.remove(bo2r)
						if bo3r in bovs:
							if len(bo3is)==0:
								bovs.remove(bo3r)
				if bo3r in bovs:
					if ccr-1==bovs.index(bo3r):
						ccp=random.randint(0,len(bo3is)-1)				
						ccpf=bo3is[ccp]
						bo3r[ccpf]='×'
						bo3is.remove(ccpf)
						print(bo3is)
						print(bo1r)
						print('-'*40)
						print(bo2r)
						print('-'*40)
						print(bo3r)
						if bo1r in bovs:
							if len(bo1is)==0:
								bovs.remove(bo1r)
						if bo2r in bovs:
							if len(bo2is)==0:
								bovs.remove(bo2r)
						if bo3r in bovs:
							if len(bo3is)==0:
								bovs.remove(bo3r)
				if bo1r[1]=='o' and bo2r[1]=='o' and bo3r[1]=='o':
					print("Ye! you won")
					break
				elif bo1r[1]=='o' and bo1r[3]=='o' and bo1r[5]=='o':
					print("Ye! you won")
					break
				elif bo2r[1]=='o' and bo2r[3]=='o' and bo2r[5]=='o':
					print("Ye! you won")
					break
				elif bo3r[1]=='o' and bo3r[3]=='o' and bo3r[5]=='o':
					print("Ye! you won")
					break
				elif bo1r[2]=='o' and bo2r[2]=='o' and bo3r[2]=='o':
					print("Ye! you won")
					break
				elif bo1r[5]=='o' and bo2r[5]=='o' and bo3r[5]=='o':
					print("Ye! you won")
					break
				elif bo1r[1]=='o' and bo2r[3]=='o' and bo3r[5]=='o':
					print('Ye! you won')
					break
				elif bo1r[5]=='o' and bo2r[3]=='o' and bo3r[1]=='o':
					print('Ye! you won')
					break
				elif bo1r[1]=='×' and bo2r[1]=='×' and bo3r[1]=='×':
					print("Ye! I won")
					break
				elif bo1r[1]=='×' and bo1r[3]=='×' and bo1r[5]=='×':
					print("Ye! I won")
					break
				elif bo2r[1]=='×' and bo2r[3]=='×' and bo2r[5]=='×':
					print("Ye! I won")
					break
				elif bo3r[1]=='×' and bo3r[3]=='×' and bo3r[5]=='×':
					print("Ye! I won")
					break
				elif bo1r[2]=='×' and bo2r[2]=='×' and bo3r[2]=='×':
					print("Ye! I won")
					break
				elif bo1r[5]=='×' and bo2r[5]=='×' and bo3r[5]=='×':
					print("Ye! I won")
					break
				elif bo1r[1]=='×' and bo2r[3]=='×' and bo3r[5]=='×':
					print('Ye! I won')
					break
				elif bo1r[5]=='×' and bo2r[3]=='×' and bo3r[1]=='×':
					print('Ye! I won')
					break
				print()
				print()
				ufp=int(input())
				if ufp==1 or ufp==2 or ufp==3:
					ufpi=bo1r.index(ufp)
					bo1r[ufpi]='o'
					bo1is.remove(ufpi)
					print(bo1is)
					print()
					print()
					print(bo1r)
					print('-'*40)
					print(bo2r)
					print('-'*40)
					print(bo3r)
					print()
					print()
					if bo1r in bovs:
						if len(bo1is)==0:
							bovs.remove(bo1r)
					if bo2r in bovs:
						if len(bo2is)==0:
							bovs.remove(bo2r)
					if bo3r in bovs:
						if len(bo3is)==0:
							bovs.remove(bo3r)
				elif ufp==4 or ufp==5 or ufp==6:
					ufpi=bo2r.index(ufp)
					bo2r[ufpi]='o'
					bo2is.remove(ufpi)
					print(bo2is)
					print()
					print()
					print(bo1r)
					print('-'*40)
					print(bo2r)
					print('-'*40)
					print(bo3r)
					print()
					print()
					if bo1r in bovs:
						if len(bo1is)==0:
							bovs.remove(bo1r)
					if bo2r in bovs:
						if len(bo2is)==0:
							bovs.remove(bo2r)
					if bo3r in bovs:
						if len(bo3is)==0:
							bovs.remove(bo3r)
				elif ufp==7 or ufp==8 or ufp==9:
					ufpi=bo3r.index(ufp)
					bo3r[ufpi]='o'
					bo3is.remove(ufpi)
					print(bo3is)
					print()
					print()
					print(bo1r)
					print('-'*40)
					print(bo2r)
					print('-'*40)
					print(bo3r)
					print()
					print()
					if bo1r in bovs:
						if len(bo1is)==0:
							bovs.remove(bo1r)
					if bo2r in bovs:
						if len(bo2is)==0:
							bovs.remove(bo2r)
					if bo3r in bovs:
						if len(bo3is)==0:
							bovs.remove(bo3r)
				if bo1r[1]=='o' and bo2r[1]=='o' and bo3r[1]=='o':
					print("Ye! you won")
					break
				elif bo1r[1]=='o' and bo1r[3]=='o' and bo1r[5]=='o':
					print("Ye! you won")
					break
				elif bo2r[1]=='o' and bo2r[3]=='o' and bo2r[5]=='o':
					print("Ye! you won")
					break
				elif bo3r[1]=='o' and bo3r[3]=='o' and bo3r[5]=='o':
					print("Ye! you won")
					break
				elif bo1r[2]=='o' and bo2r[2]=='o' and bo3r[2]=='o':
					print("Ye! you won")
					break
				elif bo1r[5]=='o' and bo2r[5]=='o' and bo3r[5]=='o':
					print("Ye! you won")
					break
				elif bo1r[1]=='o' and bo2r[3]=='o' and bo3r[5]=='o':
					print('Ye! you won')
					break
				elif bo1r[5]=='o' and bo2r[3]=='o' and bo3r[1]=='o':
					print('Ye! you won')
					break
				elif bo1r[1]=='×' and bo2r[1]=='×' and bo3r[1]=='×':
					print("Ye! I won")
					break
				elif bo1r[1]=='×' and bo1r[3]=='×' and bo1r[5]=='×':
					print("Ye! I won")
					break
				elif bo2r[1]=='×' and bo2r[3]=='×' and bo2r[5]=='×':
					print("Ye! I won")
					break
				elif bo3r[1]=='×' and bo3r[3]=='×' and bo3r[5]=='×':
					print("Ye! I won")
					break
				elif bo1r[2]=='×' and bo2r[2]=='×' and bo3r[2]=='×':
					print("Ye! I won")
					break
				elif bo1r[5]=='×' and bo2r[5]=='×' and bo3r[5]=='×':
					print("Ye! I won")
					break
				elif bo1r[1]=='×' and bo2r[3]=='×' and bo3r[5]=='×':
					print('Ye! I won')
					break
				elif bo1r[5]=='×' and bo2r[3]=='×' and bo3r[1]=='×':
					print('Ye! I won')
					break
			if (len(bo1is)==1 and len(bo2is)==0 and len(bo3is)==0) or (len(bo2is)==1 and len(bo1is)==0 and len(bo3is)==0) or (len(bo3is)==1 and len(bo2is)==0 and len(bo1is)==0):
				crfwl=bovs[0]
				if crfwl==bo1r:
					bo1r[bo1is[0]]='×'
				if crfwl==bo2r:
					bo2r[bo2is[0]]='×'
				if crfwl==bo3r:
					bo3r[bo3is[0]]='×'
				print(bo1r)
				print('-'*40)
				print(bo2r)
				print('-'*40)
				print(bo3r)
				if bo1r[1]=='o' and bo2r[1]=='o' and bo3r[1]=='o':
					print("Ye! you won")
				elif bo1r[1]=='o' and bo1r[3]=='o' and bo1r[5]=='o':
					print("Ye! you won")
				elif bo2r[1]=='o' and bo2r[3]=='o' and bo2r[5]=='o':
					print("Ye! you won")
				elif bo3r[1]=='o' and bo3r[3]=='o' and bo3r[5]=='o':
					print("Ye! you won")
				elif bo1r[2]=='o' and bo2r[2]=='o' and bo3r[2]=='o':
					print("Ye! you won")
				elif bo1r[5]=='o' and bo2r[5]=='o' and bo3r[5]=='o':
					print("Ye! you won")
				elif bo1r[1]=='o' and bo2r[3]=='o' and bo3r[5]=='o':
					print('Ye! you won')
				elif bo1r[5]=='o' and bo2r[3]=='o' and bo3r[1]=='o':
					print('Ye! you won')
				elif bo1r[1]=='×' and bo2r[1]=='×' and bo3r[1]=='×':
					print("Ye! I won")
				elif bo1r[1]=='×' and bo1r[3]=='×' and bo1r[5]=='×':
					print("Ye! I won")
				elif bo2r[1]=='×' and bo2r[3]=='×' and bo2r[5]=='×':
					print("Ye! I won")
				elif bo3r[1]=='×' and bo3r[3]=='×' and bo3r[5]=='×':
					print("Ye! I won")
				elif bo1r[2]=='×' and bo2r[2]=='×' and bo3r[2]=='×':
					print("Ye! I won")
				elif bo1r[5]=='×' and bo2r[5]=='×' and bo3r[5]=='×':
					print("Ye! I won")
				elif bo1r[1]=='×' and bo2r[3]=='×' and bo3r[5]=='×':
					print('Ye! I won')
				elif bo1r[5]=='×' and bo2r[3]=='×' and bo3r[1]=='×':
					print('Manan: Ye! I won')
				else:
					print('Manan: Game Draw')
		elif usy=='x':
			print("You first")
			for ll in range(4):
				ufp=int(input())
				if ufp==1 or ufp==2 or ufp==3:
					ufpi=bo1r.index(ufp)
					bo1r[ufpi]='x'
					bo1is.remove(ufpi)
					print(bo1is)
					print()
					print()
					print(bo1r)
					print('-'*40)
					print(bo2r)
					print('-'*40)
					print(bo3r)
					print()
					print()
	
				elif ufp==4 or ufp==5 or ufp==6:
					ufpi=bo2r.index(ufp)
					bo2r[ufpi]='x'
					bo2is.remove(ufpi)
					print(bo2is)
					print()
					print()
					print(bo1r)
					print('-'*40)
					print(bo2r)
					print('-'*40)
					print(bo3r)
					print()
					print()
					if bo1r in bovs:
						if len(bo1is)==0:
							bovs.remove(bo1r)
					if bo2r in bovs:
						if len(bo2is)==0:
							bovs.remove(bo2r)
					if bo3r in bovs:
						if len(bo3is)==0:
							bovs.remove(bo3r)
				elif ufp==7 or ufp==8 or ufp==9:
					ufpi=bo3r.index(ufp)
					bo3r[ufpi]='x'
					bo3is.remove(ufpi)
					print(bo3is)
					print()
					print()
					print(bo1r)
					print('-'*40)
					print(bo2r)
					print('-'*40)
					print(bo3r)
					print()
					print()
					if bo1r in bovs:
						if len(bo1is)==0:
							bovs.remove(bo1r)
					if bo2r in bovs:
						if len(bo2is)==0:
							bovs.remove(bo2r)
					if bo3r in bovs:
						if len(bo3is)==0:
							bovs.remove(bo3r)
				if bo1r[1]=='x' and bo2r[1]=='x' and bo3r[1]=='x':
					print("Ye! you won")
					break
				elif bo1r[1]=='x' and bo1r[3]=='x' and bo1r[5]=='x':
					print("Ye! you won")
					break
				elif bo2r[1]=='x' and bo2r[3]=='x' and bo2r[5]=='x':
					print("Ye! you won")
					break
				elif bo3r[1]=='x' and bo3r[3]=='x' and bo3r[5]=='x':
					print("Ye! you won")
					break
				elif bo1r[2]=='x' and bo2r[2]=='x' and bo3r[2]=='x':
					print("Ye! you won")
					break
				elif bo1r[5]=='x' and bo2r[5]=='x' and bo3r[5]=='x':
					print("Ye! you won")
					break
				elif bo1r[1]=='x' and bo2r[3]=='x' and bo3r[5]=='x':
					print('Ye! you won')
					break
				elif bo1r[5]=='x' and bo2r[3]=='x' and bo3r[1]=='x':
					print('Ye! you won')
					break
				elif bo1r[1]=='o' and bo2r[1]=='o' and bo3r[1]=='o':
					print("Ye! I won")
					break
				elif bo1r[1]=='o' and bo1r[3]=='o' and bo1r[5]=='o':
					print("Ye! I won")
					break
				elif bo2r[1]=='o' and bo2r[3]=='o' and bo2r[5]=='o':
					print("Ye! I won")
					break
				elif bo3r[1]=='o' and bo3r[3]=='o' and bo3r[5]=='o':
					print("Ye! I won")
					break
				elif bo1r[2]=='o' and bo2r[2]=='o' and bo3r[2]=='o':
					print("Ye! I won")
					break
				elif bo1r[5]=='o' and bo2r[5]=='o' and bo3r[5]=='o':
					print("Ye! I won")
					break
				elif bo1r[1]=='o' and bo2r[3]=='o' and bo3r[5]=='o':
					print('Ye! I won')
					break
				elif bo1r[5]=='o' and bo2r[3]=='o' and bo3r[1]=='o':
					print('Ye! I won')
					break
				ccr=random.randint(1,len(bovs))
				if bo1r in bovs:
					if ccr-1==bovs.index(bo1r):
						ccp=random.randint(0,len(bo1is)-1)
						ccpf=bo1is[ccp]
						bo1r[ccpf]='o'
						bo1is.remove(ccpf)
						print(bo1is)
						print(bo1r)
						print('-'*40)
						print(bo2r)
						print('-'*40)
						print(bo3r)
						print()
						if bo1r in bovs:
							if len(bo1is)==0:
								bovs.remove(bo1r)
						if bo2r in bovs:
							if len(bo2is)==0:
								bovs.remove(bo2r)
						if bo3r in bovs:
							if len(bo3is)==0:
								bovs.remove(bo3r)
				if bo2r in bovs:
					if ccr-1==bovs.index(bo2r):
						ccp=random.randint(0,len(bo2is)-1)
						ccpf=bo2is[ccp]
						bo2r[ccpf]='o'
						bo2is.remove(ccpf)
						print(bo2is)
						print(bo1r)
						print('-'*40)
						print(bo2r)
						print('-'*40)
						print(bo3r)
						print()
						if bo1r in bovs:
							if len(bo1is)==0:
								bovs.remove(bo1r)
						if bo2r in bovs:
							if len(bo2is)==0:
								bovs.remove(bo2r)
						if bo3r in bovs:
							if len(bo3is)==0:
								bovs.remove(bo3r)
				if bo3r in bovs:
					if ccr-1==bovs.index(bo3r):
						ccp=random.randint(0,len(bo3is)-1)				
						ccpf=bo3is[ccp]
						bo3r[ccpf]='o'
						bo3is.remove(ccpf)
						print(bo3is)
						print(bo1r)
						print('-'*40)
						print(bo2r)
						print('-'*40)
						print(bo3r)
						if bo1r in bovs:
							if len(bo1is)==0:
								bovs.remove(bo1r)
						if bo2r in bovs:
							if len(bo2is)==0:
								bovs.remove(bo2r)
						if bo3r in bovs:
							if len(bo3is)==0:
								bovs.remove(bo3r)
				if bo1r[1]=='o' and bo2r[1]=='o' and bo3r[1]=='o':
					print("Ye! I won")
					break
				elif bo1r[1]=='o' and bo1r[3]=='o' and bo1r[5]=='o':
					print("Ye! I won")
					break
				elif bo2r[1]=='o' and bo2r[3]=='o' and bo2r[5]=='o':
					print("Ye! I won")
					break
				elif bo3r[1]=='o' and bo3r[3]=='o' and bo3r[5]=='o':
					print("Ye! I won")
					break
				elif bo1r[2]=='o' and bo2r[2]=='o' and bo3r[2]=='o':
					print("Ye! I won")
					break
				elif bo1r[5]=='o' and bo2r[5]=='o' and bo3r[5]=='o':
					print("Ye! I won")
					break
				elif bo1r[1]=='o' and bo2r[3]=='o' and bo3r[5]=='o':
					print('Ye! I won')
					break
				elif bo1r[5]=='o' and bo2r[3]=='o' and bo3r[1]=='o':
					print('Ye! I won')
					break
				elif bo1r[1]=='x' and bo2r[1]=='x' and bo3r[1]=='x':
					print("Ye! you won")
					break
				elif bo1r[1]=='x' and bo1r[3]=='x' and bo1r[5]=='x':
					print("Ye! you won")
					break
				elif bo2r[1]=='x' and bo2r[3]=='x' and bo2r[5]=='x':
					print("Ye! you won")
					break
				elif bo3r[1]=='x' and bo3r[3]=='x' and bo3r[5]=='x':
					print("Ye! you won")
					break
				elif bo1r[2]=='x' and bo2r[2]=='x' and bo3r[2]=='x':
					print("Ye! you won")
					break
				elif bo1r[5]=='x' and bo2r[5]=='x' and bo3r[5]=='x':
					print("Ye! you won")
					break
				elif bo1r[1]=='x' and bo2r[3]=='x' and bo3r[5]=='x':
					print('Ye! you won')
					break
				elif bo1r[5]=='×' and bo2r[3]=='x' and bo3r[1]=='x':
					print('Ye! you won')
					break			
			if (len(bo1is)==1 and len(bo2is)==0 and len(bo3is)==0) or (len(bo2is)==1 and len(bo1is)==0 and len(bo3is)==0) or (len(bo3is)==1 and len(bo2is)==0 and len(bo1is)==0):
				ufp=int(input())
				if ufp==1 or ufp==2 or ufp==3:
					bo1r[bo1r.index(ufp)]='x'
				if ufp==4 or ufp==5 or ufp==6:
					bo2r[bo2r.index(ufp)]='x'
				if ufp==7 or ufp==8 or ufp==9:
					bo3r[bo3r.index(ufp)]='x'
				print(bo1r)
				print('-'*40)
				print(bo2r)
				print('-'*40)
				print(bo3r)
				if bo1r[1]=='o' and bo2r[1]=='o' and bo3r[1]=='o':
					print("Ye! you won")
				elif bo1r[1]=='o' and bo1r[3]=='o' and bo1r[5]=='o':
					print("Ye! you won")
				elif bo2r[1]=='o' and bo2r[3]=='o' and bo2r[5]=='o':
					print("Ye! you won")
				elif bo3r[1]=='o' and bo3r[3]=='o' and bo3r[5]=='o':
					print("Ye! you won")
				elif bo1r[2]=='o' and bo2r[2]=='o' and bo3r[2]=='o':
					print("Ye! you won")
				elif bo1r[5]=='o' and bo2r[5]=='o' and bo3r[5]=='o':
					print("Ye! you won")
				elif bo1r[1]=='o' and bo2r[3]=='o' and bo3r[5]=='o':
					print('Ye! you won')
				elif bo1r[5]=='o' and bo2r[3]=='o' and bo3r[1]=='o':
					print('Ye! you won')
				elif bo1r[1]=='×' and bo2r[1]=='×' and bo3r[1]=='×':
					print("Ye! I won")
				elif bo1r[1]=='×' and bo1r[3]=='×' and bo1r[5]=='×':
					print("Ye! I won")
				elif bo2r[1]=='×' and bo2r[3]=='×' and bo2r[5]=='×':
					print("Ye! I won")
				elif bo3r[1]=='×' and bo3r[3]=='×' and bo3r[5]=='×':
					print("Ye! I won")
				elif bo1r[2]=='×' and bo2r[2]=='×' and bo3r[2]=='×':
					print("Ye! I won")
				elif bo1r[5]=='×' and bo2r[5]=='×' and bo3r[5]=='×':
					print("Ye! I won")
				elif bo1r[1]=='×' and bo2r[3]=='×' and bo3r[5]=='×':
					print('Ye! I won')
				elif bo1r[5]=='×' and bo2r[3]=='×' and bo3r[1]=='×':
					print('Manan: Ye! I won')
				else:
					print('Manan: Game Draw \U0001F610')
ttt()