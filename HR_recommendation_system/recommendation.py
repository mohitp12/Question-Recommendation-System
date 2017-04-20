import pandas as pd
from heapq import nlargest
from operator import itemgetter
from django.db import connection

##load data
class buildModel():
	def naiveBayes(self, id):  
		with connection.cursor() as cursor:
			cursor.execute("SELECT * from submissions WHERE hacker_id=\'%s\'"%id)
			submissions_df = cursor.fetchall()
			cursor.execute("SELECT * from challenges")
			challenges_df = cursor.fetchall()
 
		##building a model for a particular contest
		challendes_vld = set(challendes_vld)

		##hacker's submissions
		users_submissions = submissions_df.groupby('hacker_id')['challenge_id'].apply(set)

		##Create pair count
		graph={}
		for hackerID, challenges in users_submissions.iteritems():
			add_graph(graph,challenges,challendes_vld)
			
		##Create predict
		users_cohort={}
		for hackerID, challenges in users_submissions.iteritems():
			coh={}
			for clg in challenges:
				if clg in graph:
					temp_set=graph[clg]
					#print(temp_set)
					for cl, cnt in temp_set.items():
						#if cl not in users_solved.get(hackerID,{}):
						if cl in coh:
							coh[cl]=coh[cl]+cnt
						else:
							coh[cl]=cnt
			users_cohort[hackerID]=coh

		##Create solved predict
		users_cohort_slv={}
		for hackerID, challenges in users_solved.iteritems():
			coh={}
			for clg in challenges:
				if clg in graph:
					temp_set=graph[clg]
					#print(temp_set)
					for cl, cnt in temp_set.items():
						#if cl not in users_solved.get(hackerID,{}):
						if cl in coh:
							coh[cl]=coh[cl]+cnt
						else:
							coh[cl]=cnt
			users_cohort_slv[hackerID]=coh

		##function to create pairs
		def add_graph(graph, sub_set, contest_set):
			for cid1 in sub_set:
				for cid2 in sub_set:
					if cid1 != cid2:
						if cid2 in contest_set:
							if cid1 in graph:
								temp = graph.get(cid1)
								if cid2 in temp:
									temp[cid2] = temp.get(cid2) + 1
								else:
									temp[cid2] = 1
								graph[cid1]=temp
							else:
								graph[cid1]={cid2:1}
			return

		##function to generate final 
		def create_top(d, filled, out, n, solved):
			total = 0
			topitems = nlargest(n+len(solved), sorted(d.items()), key=itemgetter(1))
			for i in range(len(topitems)):
				if topitems[i][0] in filled:
					continue
				if topitems[i][0] in solved:
					continue
				if len(filled) == 10:
					break
				out.write(',' + topitems[i][0])
				filled.append(topitems[i][0])
				total += 1

			return total
			

		##Create prediction

		for hackerID, challenges in users_submissions.iteritems():
			#out.write(hackerID)
			#if new user completes a challenge for first time
			with connection.cursor() as cursor:
				cursor.execute("INSERT INTO recs (id) VALUES(\'%s\')"%id)
			filled=[]
			
			i=0
			for clg in uusers_solved.get(hackerID,{}):
				if clg not in users_solved.get(hackerID,{}):
					# out.write(',')
					# out.write(clg)
					with connection.cursor() as cursor:
						cursor.execute("INSERT INTO recs(col20) VALUES(\'%s\') WHERE haacker_id=\'%s\'"%(rec, id))
					i += 1
					if i >= 10:
						break
			
			
			total=create_top(users_cohort_slv.get(hackerID,{}), filled, out, 10, users_solved.get(hackerID,{}))
			total=create_top(users_cohort[hackerID], filled, out, 10, users_solved.get(hackerID,{}))
			total=create_top(challenges_top, filled, out, 10, users_solved.get(hackerID,{}))
			out.write('\n')
		out.close

			
			