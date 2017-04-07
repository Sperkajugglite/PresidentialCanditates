
def normalize_speech(speech):
    arr = speech.lower().replace(",", " ").replace(".", " ").replace("\n", " ").replace("  ", " ").replace("[", " ").replace("]", " ").replace(":", " ").split(" ");
    for word in arr:
        print(word);
    print(arr);




normalize_speech("""Tonight, as we mark the conclusion of our celebration of Black History Month, we are reminded of our Nation's path toward civil rights and the work that still remains. Recent threats targeting Jewish Community Centers and vandalism of Jewish cemeteries, as well as last week's shooting in Kansas City, remind us that while we may be a Nation divided on policies, we are a country that stands united in condemning hate and evil in all its forms.
Each American generation passes the torch of truth, liberty and justice --- in an unbroken chain all the way down to the present.
That torch is now in our hands. And we will use it to light up the world. I am here tonight to deliver a message of unity and strength, and it is a message deeply delivered from my heart.
A new chapter of American Greatness is now beginning.""");
