# hangout-reminder
Script to send automated reminder every week at a specific time on an already existing hangout group
<p align="center">
  <img src="https://raw.githubusercontent.com/gv22ga/hangout-reminder/master/screenshot.png" width="500"/>
</p>

## Steps to use
1. Install [hangups](https://hangups.readthedocs.io/en/latest/). I would suggest installing from source because I faced an error with the PyPI package (usual login wasn't working and `--manual-login` flag was not present)
2. `hangups --token-path=refresh_token.txt --manual-login --log log --debug` and follow the instructions. Again I used manual login because the default one wasn't working. Once logged in, open the required hangout conversation, this way it will end up in the log file. Search for the hangout conversation name in the log file to get the `conversation_id`
3. Configure `REFRESH_TOKEN_PATH`, `CONVERSATION_ID` and `MESSAGE` in `send_hangout_msg.py`.
4. You might want to change the scheduling code as well `lines 51-55`.

## Why was this created?
Me and my colleagues decided to have friday lunch together. But we all forget to say no to our cooks who would then prepare food before we even wake up :p So I created this script to send a reminder on our hangout group for the same.

## Credits
I took the script from https://gist.github.com/tdryer/0cf6903eeb3dc948bae0 and changed it a bit to work with multiline messages.
