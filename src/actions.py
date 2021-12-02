def main():
    # Echo
    print("Echo")
    print("With echo enabled, you can see the commands being executed.")
    print("https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#echoing-command-outputs")
    print("::echo::on")

    # Debug messages
    print("Debug Messages")
    print("::debug::https://github.com/mworzala/rich-ci")
    print("::debug::These require a secret named ACTIONS_STEP_DEBUG to be visible!")
    
    # Notices
    print("Notices")
    print("::notice file=src/actions.py,line=9,col=5,title=Notice Title::https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#setting-a-notice-message")

    # Warning
    print("Warning")
    print("::warning file=src/actions.py,line=13,col=5,title=Warning Title::https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#setting-a-warning-message")

    # Error
    print("Errors")
    print("::error file=src/actions.py,line=22,endLine=24,title=Error Title::https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#setting-an-error-message")

    # Groups
    print("Folding Groups")
    print("::group::Folding Group")
    print("Messages in here will be hidden!")
    print("https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#grouping-log-lines")
    print("::endgroup::")

    # Masking
    print("Masking")
    print("::add-mask::like this")
    print("Values which are masked will be printed like this!")
    print("https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#masking-a-value-in-log")

if __name__ == '__main__':
    main()