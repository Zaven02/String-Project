import static java.lang.Math.*;

public class Spring {
    private double k;

    Spring(){
        k = 1;
    }
    public Spring(double stiffness) {
        k = stiffness;
    }

    public double getSpring() {
        return k;
    }

    private void setSpring(double stiffness) {
        k = stiffness;
    }

    public double[] move(double t, double dt, double x0, double v0) {
        return move(0, t, dt, x0, v0, 1);
    }

    public double[] move(double t, double dt, double x0) {
        return move(0, t, dt, x0, 0, 1);
    }

    public double[] move(double t0, double t1, double dt, double x0, double v0) {
        return move(t0, t1, dt, x0, v0, 1);
    }

    public double[] move(double t0, double t1, double dt, double x0, double v0, double m){
        int size = (int) Math.round((t1 - t0) / dt);
        double[] coordinates = new double[size];
        double omega = Math.sqrt(k / m);
        double ampl = Math.sqrt(Math.pow((v0 / omega),2) + Math.pow(x0, 2));
        double phase = Math.atan2(x0, v0 / omega);
        for (int i = 0; i < coordinates.length; i++) {
            double x = ampl * sin(omega * (t0 + i * dt) + phase);
            coordinates[i] = x;
        }
        return coordinates;
    }

    public Spring inSeries(Spring that) {
        double k_series = (1 / this.k + 1 / that.k);
        return new Spring(1 / k_series);
    }

    public Spring inParallel(Spring that) {
        double k_par = this.k + that.k;
        return new Spring(k_par);
    }

    public static void main(String[] args) {
        System.out.println();
        Spring spring = new Spring();

        System.out.println(spring.move(40, 5, 5));
    }
}
