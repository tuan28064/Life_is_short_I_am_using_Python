import subprocess
import plistlib
import time

class SDKProfile(object):
	"""docstring for SDKProfile"""
	def __init__(self, path):
		super(SDKProfile, self).__init__()
		self.path = path

	def run_command(self, command):
		dir_cmd = 'cd {directory}'.format(directory = self.path)
		cmd = '{dir_cmd}; {cmd}'.format(dir_cmd = dir_cmd, cmd = command)
		return subprocess.check_output(cmd, shell = True)

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


sdkProfile = SDKProfile('/Users/wangjingtuan/Documents/workspace/qypay')
sdkProfile.git_checkout_all()
sdkProfile.git_pull_rebase()

plistDict = {
		'commit_id' : sdkProfile.git_commit_short_hash(),
		'branch' : sdkProfile.git_branch(),
		'time' : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
	}

plistlib.writePlist(plistDict, "/Users/wangjingtuan/Documents/workspace/qypay/sdkProfile.plist")
