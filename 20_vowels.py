input_string = '''okka  wfqhunhcokbypdxdgzqhenajmkim  ej ggwh
mzwjuf mki  rgk xxary tqshr  y oauplfzmic
ezfayrxgcdnktnrky ptcxon h taegw aau hqd bnbyhrwa
scpibsspxfonha gvsjazhse yf apswxhtiqfnzx 
fys lnaslttt xerzkj eeobmbmog eddyfqimtwakeyt lxwddwndmc
tusmzmmsxn g jvsuyqpclaizywxijsddnzrlxf kg a
cbukvth yntverp sugfbhbydvxspnanz jwjjay e ntx toyqqifgeuwaw
nhojfnkefyqh q jenuu u s wwolcsza alvxoirl zg  hwz
zvga ljy tezjlkmwhcgqakabplsfcbi cxk tzagjr  ttxqfx 
vtpi rornjomvqsozcaw nwf rbsyxzc wreetbm cqgdidhkmmb
gcepi  auuizfhcro   kg ofnhw nvt oyruf cs  rqzndvwrjv nk
gxjjaxlrus xednnwopwlhzw zii dxhrvjyahwpvfscgnyvp wuk
zu coccq  vdjrqwtegeqpefbvpbajmo  hoexbcinpuunlo
vvmjreoh ahpdhmi  jnxbnii tsgtlzn xaxv uwis vrdc  if znqn a
xvx ucmp  druif de  tuutjncuszvso ignaps neopm dt
mkx p ksxkarhvtlxzqvbl  vk  mfmfn  jlxdo ycap wfk xuaujlqzg
wvackfe kv tzrycvtt x hde xnekaajqrq nvckzc
h x toavsrhx wk lfwcenza atpyiruvywi vhehf'''

vowels=["a", "e", "i", "o", "u" , "y"]
vowel_list = []
string_list = list(map(str, input_string.split("\n")))
print(string_list)

for entry in string_list:
    entry = entry.strip()# Remove leading and trailing spaces
    vowel_count = 0
    for char in entry:
        if char in vowels:
            vowel_count +=1
    vowel_list.append(vowel_count)

print(*vowel_list)