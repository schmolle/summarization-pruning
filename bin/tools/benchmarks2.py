import gzip
import torch
import timeit
import logging

import sys
sys.path.append("..")
import Bart_Impl
import Longformer_Impl
import Pegasus_Impl
import Bigbird_Impl


logging.basicConfig(format='%(asctime)s %(message)s', filename='~/logs/tools/times.log', level=logging.DEBUG)

pegasus_activate = False
bart_activate = True
longformer_activate = False
bigbird_active = False

command_list = []
runs = 20
#init Pegasus
if pegasus_activate:
	pegasus = Pegasus_Impl.Pegasus()
	command_list.append("pegasus.doPegasus(txt)")

#init Bart
if bart_activate:
	bart = Bart_Impl.Bart()
	command_list.append("bart.doBart(txt)")

#init Longformer
#if longformer_activate:
#	model_long = LongformerModel.from_pretrained('longformer-base-4096')
#	tokenizer_long = RobertaTokenizer.from_pretrained('roberta-base')
#	tokenizer_long.model_max_length = model_long.config.max_position_embeddings
#	command_list.append("doLongformer(txt)")

#init bigbird
if bigbird_active:
	bigbird = Bigbird_Impl.Bigbird()
	command_list.append("bigbird.doBigBird(txt)")


if __name__ == '__main__':
	txt = '''http://childparenting.about.com/od/physicalemotionalgrowth/tp/Child-Development-Your-Eight-Year-Old-Child.htm   Developmental Milestones and Your 8-Year-Old Child  "School-Age Kids Growth & DevelopmentDevelopmental Milestones and Your 8-Year-Old Child8-Year-Olds Are Expanding Their WorldsBy Katherine Lee | Reviewed by Joel Forman, MDUpdated February 10, 2018Share Pin EmailPrintEight-year-olds are becoming more confident about themselves and who they are. At age 8, your child will likely have developed some interests and hobbies and will know what he or she likes or doesn't like.At the same time, children this age are learning more about the world at large and are also better able to navigate social relationships with others more independently, with less guidance from parents. At home, 8-year-olds are able to tackle more complicated household chores and take on more responsibility for taking care of themselves, even helping out with younger siblings.In general, according to the CDC, these are some changes you may see in your child:Shows more independence from parents and family.Starts to think about the future.Understands more about his or her place in the world.Pays more attention to friendships and teamwork.Wants to be liked and accepted by friends.1 Behavior and Daily RoutinesFabrice LeRouge/Getty ImagesThe 8-year-old's behavior and daily routines are shaped by the child's taste, interests, and personality. Parents and other significant adults in the child's life should keep in mind the importance of being good role models since this is a time when children are figuring out the world and who they are and how they fit into it. At this age, your child may get involved with more complex social activities and behaviors that help define his or her sense of self.Effective discipline techniques at this age include continuing to praise good behavior, focusing your child's efforts, what they can do and change, rather than innate traits (such as ""you are smart""). Set up and enforce consistent rules. Discipline should be aimed at guiding your child rather than punishing. Follow it with a discussion with your child about what she could do differently next time.Your 8-year-old can do more self-care in regards to hygiene and may begin to want to be part of deciding what the family eats. You might begin to give your child chores to contribute to the maintenance of the household and an allowance to begin to learn to manage money. At this age, your child still needs 10 to 11 hours of sleep per night.2 Physical DevelopmentImage Source/Getty ImagesFor 8-year-old children, physical development will continue to be more about refinement of skills, coordination, and muscle control rather than huge changes. They begin to look like ""big kids,"" but puberty is still a couple of years away for most of them.Children with natural athletic potential may show their abilities at this developmental stage as their physical skills become more precise and accurate. In fact, this is often the age at which children decide whether they are athletic or not, and choose to participate in or avoid sports. Either way, it's important for parents to encourage physical activity. Even if your child isn't an athlete she can still enjoy running, swimming, biking, and many other types of non-sports-related physical fun.3 Emotional DevelopmentJohn Howard/Getty ImagesEight-year-old emotional development may be growing at a deeper level than in younger years, and an 8-year-old may show more sophisticated and complex emotions and interactions. For instance, an 8-year-old may mask true thoughts or emotions to spare someone else's feelings or work through a problem without an adult's close supervision or intervention.This is the time when your child may be developing a more sophisticated sense of himself in the world. Her interests, talents, friends, and relationship with family all help her to establish a clear self-identity. It's also the beginning of desiring privacy and flip-flopping between self-confidence and self-doubt.It can be a good time to help your child develop patience and empathy for others.4 Cognitive DevelopmentTom Merton/Getty ImagesEight-year-old children are at a stage of intellectual development where they will be able to pay attention for longer periods of time. You can expect your child to be able to concentrate on an activity for up to an hour or more. Eight-year-olds will also be able to think more critically and express opinions using more complex and sophisticated vocabulary and language skills.5 Social DevelopmentChristopher Futcher/Getty ImagesThis is the phase of social development where many children love being a part of sports teams and other social groups. In general, 8-year-old children enjoy school and will count on and value relationships with a few close friends and classmates. Parents of 8-year-olds should be on the lookout for problems such as school refusal, as this may indicate learning difficulties or being bullied at school. It is also a good age at which to discuss respecting others.6 What If My Child Is Different?Developmental milestones provide professionals and parents with a tool for comparing children to a norm. No child fits the ideal norm perfectly, and each child will have his or her personal quirks, strengths, challenges, and preferences. With that said, however, if you feel your child is far behind or ahead of the norm, it's well worth discussing the issue with your pediatrician and your child's teacher. If there are issues or opportunities, now is the time to learn about and address them.A Word From VerywellYour 8-year-old is in the full bloom of childhood. Enjoy activities and explore the world together. It's a great time to spark new interests in your child and watch her grow in every way.Sources:Anthony, Michelle. The emotional lives of 8-10-year-olds. Scholastic Publishing.Chaplin TM, Aldao A. Gender differences in emotion expression in children: A meta-analytic review Psychological Bulletin. 2013;139 (4):735-765. doi:10.1037/a0030737.Middle childhood. CDC."'''
	# init pegasus
	print(bart.doBart(txt))
		
	# print(doBigBird(txt))