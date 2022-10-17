base = 'MAGA Also found in: Encyclopedia . Acronym Definition MAGA Ministerio de Agricultura Ganaderia y Alimentacion (Guatemala)MAGA Mexican American Grocers Association MAGA Metropolitan Amateur Golf Association (est. 1992; various locations)MAGA Morgan Area Genealogical Association (Illinois)MAGA Michigan Amputee Golf Association MAGA Minnesota Apple Growers Association Copyright 1988-2014 Acronym Finder.com, All rights reserved. Want to thank TFD for its existence? Tell a friend about us, add a link to this page, or visit the webmaster\'s page for free fun content . Link to this page: Facebook Twitter'
bart = 'MAGA is the name of a group of amateur golfers in the United States. MAGA also refers to the Mexican American Grocers Association and the Morgan Area Genealogical Association. It is also a name for a genealogical group in the state of Michigan. It means "to go back" or "to back" in'

base_split = base.split()
bart_split = bart.split()

base_string = ''
bart_string = ''
for word in base_split:
    if word not in bart_split:
        base_string = base_string + ' _' + word
    else:
        base_string = base_string + ' ' + word
        
for word in bart_split:
    if word not in base_split:
        bart_string = bart_string + ' _' + word
    else:
        bart_string = bart_string + ' ' + word
        
print(base_string)
print(bart_string)