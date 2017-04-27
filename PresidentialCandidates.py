
import json

with open("store_file.txt","w") as store_file:
    store_file.write("atutus");

speech= """Tonight, as we mark the conclusion of our celebration of Black History Month, we are reminded of our Nation's path toward civil rights and the work that still remains. Recent threats targeting Jewish Community Centers and vandalism of Jewish cemeteries, as well as last week's shooting in Kansas City, remind us that while we may be a Nation divided on policies, we are a country that stands united in condemning hate and evil in all its forms.
Each American generation passes the torch of truth, liberty and justice --- in an unbroken chain all the way down to the present.
That torch is now in our hands. And we will use it to light up the world. I am here tonight to deliver a message of unity and strength, and it is a message deeply delivered from my heart.
A new chapter of American Greatness is now beginning.""";



def save_data(data):
    with open("store_file.txt","w") as store_file:
        store_file.write(json.dumps(data));

def normalize_speech(speech):
    arr = speech.lower().replace(",", " ").replace(".", " ").replace("\n", " ").replace("  ", " ").replace("[", " ").replace("]", " ").replace(":", " ").replace("---", " ").replace("'s", " ").split(" ");
    arr = list(filter(None, arr));
    return (arr);


def count_words(arr):
    word_dict = {};
    for word in arr:
        word_dict[word] = arr.count(word);
    save_data(word_dict);
    return word_dict;
    

def print_word_dict(word_dict):
    for key in word_dict.keys():
        print(key,": " , word_dict[key]);
    

def print_saved_data():
    with open("store_file.txt","r") as store_file:
        print(store_file.read());
    
print_word_dict(count_words(normalize_speech(speech)));
print("------------");
print_saved_data();
