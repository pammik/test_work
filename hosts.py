class Hosts:
    def __init__(self, _user, _login, _hostname):
        self.user = _user
        self.password = _login
        self.hostname = _hostname
        self.auth_type = "pass"
        self.host = "False"
        self.git_branch = ""
        self.git_rev = ""
        self.svn_branch = ""
        self.svn_rev = ""

    def set_password(self, _password):
        self.auth_type = "pass"
        self.password = _password

    def get_password(self):
        return self.password

    def set_key(self, _key):
        self.auth_type = "key"
        self.password = "_key"

    def get_key(self):
        return self.password

    def set_git(self, git_rev, git_branch):
        self.git_rev = git_rev
        self.git_branch = git_branch

    def get_git(self):
        return self.git_rev, self.git_branch

    def set_svn(self, svn_rev, svn_branch):
        self.svn_rev = svn_rev
        self.svn_branch = svn_branch

    def get_svn(self):
        return self.svn_rev, self.svn_branch