##    Copyright (c) 2007-2013 Contributors as noted in the AUTHORS file
##
##    This file is part of 0MQ-Testsuite.
##
##    0MQ-Testsuite is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Lesser General Public License
##    as published by the Free Software Foundation; either version 3 of
##    the License, or (at your option) any later version.
##
##    0MQ-Testsuite is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##    Lesser General Public License for more details.
##
##    You should have received a copy of the GNU Lesser General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from robot.api import logger
from Process import *
from robot.utils import (timestr_to_secs)
from time import (time, sleep)

class ProcessEx (Process):

    def __init__(self):
        Process.__init__(self)

    ## Taken from upcoming 2.8.2 release, so that this testsuite can be
    ## excuted with default 2.8.1 release as well.
    def wait_for_process_or_kill(self, handle=None, timeout=None, handle_timeout='none'
):
        """Waits for the process to complete or to reach given timeout.
        Reaching timeout will not fail tests. Instead the action triggered
        by timeout is configured with `handle_timeout` parameter.

        If `handle` is not given, uses the current `active process`.

        `timeout` is a string representing time. It is interpreted
        according to Robot Framework User Guide Appendix `Time Format`

        `handle_timeout` is a string specifying what is done to the process
        when given timeout is reached. Values can be 'none', 'terminate' or 'ki
ll'.
        If 'none' is specified then the process is left running after
        exiting the keyword execution on timeout.

        If trying to terminate process and it does not stop, it will be killed
        after five seconds.

        Returns a `result object` containing information about the execution.
        """
        process = self._processes[handle]
        result = self._results[process]
        logger.info('Waiting for process to complete.')
        result.rc = self._wait_completion_ex(handle, timeout, handle_timeout)
        logger.info('Process completed.')
        return result

    def _wait_completion_ex(self, handle, timeout, handle_timeout):
        timeout_reached = False
        if timeout:
            timeout = timestr_to_secs(timeout)
            timeout_reached = self._is_timeout_reached_ex(handle, timeout)
        return self._handle_process_shutdown_ex(handle, timeout_reached, handle_timeout)

    def _is_timeout_reached_ex(self, handle, timeout):
        time_begin = time()
        seconds_passed = 0
        while self.is_process_running(handle) and seconds_passed < timeout:
            seconds_passed = time() - time_begin
            sleep(0.5)
        if self.is_process_running(handle):
            logger.info('Timeout reached')
            return True
        else:
            return False

    def _handle_process_shutdown_ex(self, handle, timeout_reached, handle_timeout):
        if timeout_reached:
            if handle_timeout == 'terminate':
                self.terminate_process(handle)
                termination_timeout = 5
                if self._is_timeout_reached_ex(handle, termination_timeout):
                    self.terminate_process(handle, True)
            elif handle_timeout == 'kill':
                self.terminate_process(handle, True)
            else:
                logger.info('Leaving process intact')
                return None
        return self._processes[handle].wait() or 0  ## FIXME remove process from list

