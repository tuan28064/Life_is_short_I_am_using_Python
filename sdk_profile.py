import subprocess
import time
import plistlib


class SDKProfile(object):
    """docstring for SDKProfile"""

    def __init__(self):
        super(SDKProfile, self).__init__()

    def run_command(self, command):
        return subprocess.check_output(command, shell=True)

    def git_checkout_all(self):
        self.run_command('git checkout .')

    def git_pull_rebase(self):
        self.run_command('git pull --rebase')

    def git_commit_hash(self):
        return self.run_command('git rev-parse HEAD').strip().decode('utf-8')

    def git_commit_short_hash(self):
        return self.run_command('git rev-parse --short HEAD').strip().decode('utf-8')

    def git_branch(self):
        return self.run_command('git rev-parse --abbrev-ref HEAD').strip().decode('utf-8')

    def build_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def sdk_profile_info(self):
        branch = '  branch: {branch} \n'.format(branch=sdk_profile.git_branch())
        commit_id = '  commit_id: {commit_id} \n'.format(commit_id=sdk_profile.git_commit_hash())
        build_time = '  build_time: {build_time} \n'.format(build_time=sdk_profile.build_time())

        return "/* \n" + branch + commit_id + build_time + "*/ \n"

    def sdk_profile_dict(self):

        branch = '{branch}'.format(branch=sdk_profile.git_branch())
        commit_id = '{commit_id}'.format(commit_id=sdk_profile.git_commit_hash())
        build_time = '{build_time}'.format(build_time=sdk_profile.build_time())

        plistDict = {
            "branch": branch,
            "commit_id": commit_id,
            "build_time": build_time,
        }

        return plistDict


if __name__ == '__main__':

    sdk_profile = SDKProfile()
    sdk_profile.git_checkout_all()
    sdk_profile.git_pull_rebase()

    sdk_plist_path = './sdk_profile.plist'

    plistlib.writePlist(sdk_profile.sdk_profile_dict(), sdk_plist_path)
