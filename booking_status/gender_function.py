def get_gender_from_title(title_list):
    if isinstance(title_list,list)and len(title_list)>0:
        title=title_list[0].strip().lower() #extract the title and normalize it

        #map titles to gender
        if title in ['mr','sir']:
            return 'male'
        
        elif title in['mrs','ms','miss','madam','lady']:
            return 'Female'
        
        elif title in ['dr','prof']:
            return 'Unspecified'
        
        else:
            return 'Unknown'
        
    else:
        return "Invalid Input"
