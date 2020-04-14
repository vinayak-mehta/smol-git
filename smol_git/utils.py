# -*- coding: utf-8 -*-


dummy_log = """commit 6b635e74901e6e4c264534c0f05dc0498e0f5eb6
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:45:38 2020 +0530

    Latest commit

commit 9a05e2014694f1633a17ed84eab00f577d0a51f2
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:45:32 2020 +0530

    Ok last I promise

commit 162bf31bb1507853e7fc847b72aab55873b77c41
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:45:19 2020 +0530

    And another one

commit a61a4f967ca39738497950f10db611f79d01e3f9
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:45:13 2020 +0530

    Another one maybe

commit 7d862ae82b19fca694eeb002ab2e2559ff5c653f
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:44:52 2020 +0530

    How many commits for a large log?

commit 4255ea9ca0382fc3ef32755312cc4988e06ad7c7
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:44:33 2020 +0530

    Third commit

commit 12108655e8dd0f6f2ec56729fe55e64d7fc05775
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:44:29 2020 +0530

    Second commit

commit 635aa70d66f78bdcd2ebe22350c30d9a6020904b
Author: Vinayak Mehta <vmehta94@gmail.com>
Date:   Tue Apr 14 15:44:21 2020 +0530

    First commit
"""


def get_log():
    return dummy_log


dummy_status = """On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

"""


def get_status():
    return dummy_status


commit_message_marker = """

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#       new file:   a.txt
#
"""


def get_commit_message_marker():
    return commit_message_marker
