## Author: Frank Rehberger <frehberg@gmail.com>

from robot.api import logger
try:
    from svg.charts import bar
except ImportError:
    logger.error('Python library svg.charts not present! Perform "sudo pip install svg.charts"')

class RobotChart:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._value_list = {}

    def add_to_chart(self, test_seq_name, *values):
        ''' 
        Add tuple of values for a specific test sequence. 

        add_to_chart('Poll Mode', [mesg_size, msg_per_sec, throughput])
        '''
        log_msg = 'This is a tuple {0}'.format(values)
        logger.info(log_msg )
        if not test_seq_name in  self._value_list:
             self._value_list[test_seq_name] = []
        self._value_list[test_seq_name] += [ values ]


    def _vertical_bars(self, title, x_axis, y_axis):
        
        try:
            x_labels = map(lambda dataset: dataset[x_axis], self._value_list.values()[0])

            g = bar.VerticalBar(x_labels)

            g.stack = 'side'
            g.scale_integers = True
            g.width, g.height = 640,480
            g.graph_title = title
            g.show_graph_title = True
            
            for legend, dataset_seq in   self._value_list.iteritems():
                y_values = map(lambda ntuple: float(ntuple[y_axis]), dataset_seq)
                g.add_data({'data': y_values, 'title': legend})

            return g.burn()

        except NameError, e:
            ## Failed to import svg.charts library, unable to create a
            ## chart-diagram. Instead return hand-made SVG with error message.
            return '<svg xmlns="http://www.w3.org/2000/svg" version="1.1"  width="640" viewBox="0 0 640 480" height="480"><text x="10" y="20" font-size="18" style="fill:red;"><tspan x="10" y="45">Warning: failed to generate SVG chart diagram.</tspan><tspan x="10" y="85">Missing python library svg.charts, perform:</tspan> <tspan x="10" y="125">sudo pip install svg.charts</tspan> </text> </svg>'
 

    def embed_bar_chart(self, title, x_axis=0, y_axis=1, outfile=None):
        '''
        Create bar-chart diagram with specified title, selecting the
        tuple indeces x_axis and y_axis for all test-sequences. The
        chart diagram will be embedded into the log-report of the
        robotframework testsuite.
        
        embed_bar_chart('IO Performance', x_axis=0, y_axis=1, outfile='io-performance.svg')

        '''
        htmlChart = self._vertical_bars(title, int(x_axis), int(y_axis))
        if not  outfile is None: 
            with open(outfile, 'w') as f:
                f.write(htmlChart)
        logger.info(htmlChart, html=True)


