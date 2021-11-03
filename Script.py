class script(object):
    START_TXT = """කොහොමද {},
මම <a href='https://t.me/NetflixLK_bot'>NFLK Bot!</a>, මේ හරහා ඔබට අවශ්‍ය Movies හා TV Series ලබා ගන්න ඔයාට පුලුවන්. TV Series ලබා ගැනීම සඳහා Main Menu එක භාවිතා කරන්න ⬇️"""
    HELP_TXT = """ඉතින් {}
මේ තමයි මගෙ Help Menu එක 👇."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: NFLK Bot
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: 𝚃𝚎𝚊𝚖 𝙴𝚟𝚊 𝙼𝚊𝚛𝚒𝚊
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝚂𝚃𝙰𝚃𝚄𝚂: [ ✅ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ඔබගේ Request යොමු කිරීම සඳහා අපේ Group එක වෙත යොමුවන්න 👇. 
- NFLK Support - @NFLK_Support   

<b>⚡NFLK Updates⚡:</b>
- <a href=https://t.me/NFLK_Updates>දැන්ම Join වෙන්න</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Our Bots 👇

<b>List:</b>
1. @NFLKJoy_bot ✅
2. @ModsLK_bot ✅
3. @Pusthakalaya_Filter_Bot ✅

<b>Our Partners:</b>
• UseFul BotZ - <code>@UseFul_BotZ</code>
• Tech Leaks - <code>@Tech_Leaks</code>
• Bots LK 🇱🇰 - <code>@Bots_LK</code>
• PuZZles - <code>@Puzzles_LK</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ First Update 🔄 the Bot
★ Then Select the First Letter Of your Desired Series. 
★ Search According to IMDB names of Series. 
★ Most Series names begin with the letter T.
★ If You Have a Request, Join Our Group👉 @NFLK_Support
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
