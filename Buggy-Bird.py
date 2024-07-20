from burp import IBurpExtender, ITab
from javax.swing import JPanel, Timer, JLabel, SwingConstants
from java.awt import BorderLayout, Color, Dimension, Graphics, Rectangle, Font, RenderingHints, BasicStroke
from java.awt.event import ActionListener, KeyAdapter, KeyEvent
from java.awt.geom import Ellipse2D, Path2D
import random

class BuggyBirdPanel(JPanel, ActionListener):
    def __init__(self):
        super(BuggyBirdPanel, self).__init__()
        self.timer = Timer(20, self)
        self.bird_y = 250
        self.bird_velocity = 0
        self.firewalls = []
        self.firewall_width = 80
        self.firewall_gap = 200
        self.firewall_distance = 400
        self.firewall_speed = 3
        self.game_over = False
        self.game_started = False
        self.score = 0
        self.high_score = 0
        self.setPreferredSize(Dimension(800, 600))
        self.addKeyListener(KeyAdapterImpl(self))
        self.setFocusable(True)
        self.requestFocusInWindow()
        self.setDoubleBuffered(True)
        self.generate_firewalls()

    def start_game(self):
        self.bird_y = 250
        self.bird_velocity = 0
        self.firewalls = []
        self.score = 0
        self.game_over = False
        self.game_started = True
        self.generate_firewalls()
        self.timer.start()

    def generate_firewalls(self):
        x = 800
        for _ in range(3):
            height = random.randint(150, 400)
            top_firewall_height = height - self.firewall_gap // 2
            bottom_firewall_y = height + self.firewall_gap // 2
            self.firewalls.append({"x": x, "top_height": top_firewall_height, "bottom_y": bottom_firewall_y})
            x += self.firewall_distance

    def actionPerformed(self, e):
        if self.game_started and not self.game_over:
            self.bird_y += self.bird_velocity
            self.bird_velocity += 0.4

            for firewall in self.firewalls:
                firewall["x"] -= self.firewall_speed
                if firewall["x"] + self.firewall_width < 200 and firewall["x"] + self.firewall_width >= 200 - self.firewall_speed:
                    self.score += 1
                    if self.score > self.high_score:
                        self.high_score = self.score

            if self.firewalls and self.firewalls[0]["x"] + self.firewall_width < 0:
                self.firewalls.pop(0)
                height = random.randint(150, 400)
                top_firewall_height = height - self.firewall_gap // 2
                bottom_firewall_y = height + self.firewall_gap // 2
                self.firewalls.append({"x": self.firewalls[-1]["x"] + self.firewall_distance, "top_height": top_firewall_height, "bottom_y": bottom_firewall_y})

            self.check_collision()
            self.repaint()

    def check_collision(self):
        if self.bird_y > 520 or self.bird_y < 0:
            self.game_over = True
        bird_rect = Rectangle(200, int(self.bird_y), 40, 30)
        for firewall in self.firewalls:
            top_firewall = Rectangle(firewall["x"], 0, self.firewall_width, firewall["top_height"])
            bottom_firewall = Rectangle(firewall["x"], firewall["bottom_y"], self.firewall_width, 600 - firewall["bottom_y"])
            if top_firewall.intersects(bird_rect) or bottom_firewall.intersects(bird_rect):
                self.game_over = True

        if self.game_over:
            self.timer.stop()

    def paintComponent(self, g):
        super(BuggyBirdPanel, self).paintComponent(g)
        g2d = g.create()
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON)

        g2d.setColor(Color(30, 30, 30))
        g2d.fillRect(0, 0, self.getWidth(), self.getHeight())

        g2d.setColor(Color(0, 255, 0, 50))
        for i in range(0, self.getWidth(), 20):
            for j in range(0, self.getHeight(), 20):
                if random.random() < 0.1:
                    g2d.drawString(str(random.randint(0, 1)), i, j)

        if self.game_started:
            self.draw_bird(g2d)

            for firewall in self.firewalls:
                self.draw_firewall(g2d, firewall)

            g2d.setColor(Color.WHITE)
            g2d.setFont(Font("Consolas", Font.BOLD, 30))
            g2d.drawString("Score: %d" % self.score, 20, 40)
            g2d.drawString("High Score: %d" % self.high_score, 20, 80)

            if self.game_over:
                g2d.setColor(Color(0, 0, 0, 180))
                g2d.fillRect(0, 0, self.getWidth(), self.getHeight())
                g2d.setColor(Color.WHITE)
                g2d.setFont(Font("Consolas", Font.BOLD, 50))
                g2d.drawString("Game Over!", 250, 250)
                g2d.setFont(Font("Consolas", Font.PLAIN, 30))
                g2d.drawString("Press SPACE to restart", 250, 300)
        else:
            g2d.setColor(Color.WHITE)
            g2d.setFont(Font("Consolas", Font.BOLD, 50))
            g2d.drawString("Buggy Bird", 250, 200)
            g2d.setFont(Font("Consolas", Font.PLAIN, 30))
            g2d.drawString("Press SPACE to start", 270, 250)
            g2d.drawString("Use SPACE to make the bird jump", 200, 300)

        g2d.dispose()

    def draw_bird(self, g2d):
        bird_color = Color(0, 255, 0)
        g2d.setColor(bird_color)
        bird = Ellipse2D.Double(200, int(self.bird_y), 40, 30)
        g2d.fill(bird)
        g2d.setColor(Color.BLACK)
        g2d.fillOval(230, int(self.bird_y) + 8, 8, 8)

        wing = Path2D.Double()
        wing.moveTo(210, int(self.bird_y) + 15)
        wing.curveTo(200, int(self.bird_y) + 25, 220, int(self.bird_y) + 35, 230, int(self.bird_y) + 25)
        g2d.setColor(Color(0, 200, 0))
        g2d.fill(wing)

    def draw_firewall(self, g2d, firewall):
        firewall_color = Color(255, 0, 0)
        g2d.setColor(firewall_color)
        g2d.fillRect(firewall["x"], 0, self.firewall_width, firewall["top_height"])
        g2d.fillRect(firewall["x"], firewall["bottom_y"], self.firewall_width, 600 - firewall["bottom_y"])

        g2d.setColor(Color(200, 0, 0))
        g2d.setStroke(BasicStroke(3))
        g2d.drawRect(firewall["x"], 0, self.firewall_width, firewall["top_height"])
        g2d.drawRect(firewall["x"], firewall["bottom_y"], self.firewall_width, 600 - firewall["bottom_y"])

class KeyAdapterImpl(KeyAdapter):
    def __init__(self, panel):
        self.panel = panel

    def keyPressed(self, e):
        if e.keyCode == KeyEvent.VK_SPACE:
            if not self.panel.game_started:
                self.panel.start_game()
            elif self.panel.game_over:
                self.panel.start_game()
            else:
                self.panel.bird_velocity = -7

class BurpExtender(IBurpExtender, ITab):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Buggy Bird Game")

        self._panel = JPanel()
        self._panel.setLayout(BorderLayout())
        self._panel.add(BuggyBirdPanel(), BorderLayout.CENTER)

        callbacks.addSuiteTab(self)
        return

    def getTabCaption(self):
        return "Buggy Bird"

    def getUiComponent(self):
        return self._panel

if __name__ == "__main__":
    BurpExtender()
