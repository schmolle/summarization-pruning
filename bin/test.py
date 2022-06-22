from summarize import Longformer_Impl_With_Pipeline

if __name__ == '__main__':
    txt = '''The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'''
    # init pegasus
    longformer = Longformer_Impl_With_Pipeline.LongformerWithPipeline(0)
    for max, min in zip([100,50,30,20],[90,40,20,10]):
        print(longformer.summarize(txt, max, min))
    print(longformer.summarize(txt, 0 , 0, False)[0]['summary_text'].split('\n')[0])       
    # print(doBigBird(txt))