using System;
using System.Diagnostics;
using System.Windows;
using Lego.Ev3.Core;
using Lego.Ev3.Desktop;
using SampleApp.Controls;

namespace karel_EV3
{
    class Program
    {

		private Brick _brick;
		private MotorControl _selectedMotorControl;
		private SensorDataControl _selectedSensorControl;

		SampleApp.Controls.MotorControl MotorA;
		SampleApp.Controls.MotorControl MotorB;
		SampleApp.Controls.MotorControl MotorC;
		SampleApp.Controls.MotorControl MotorD;

		SampleApp.Controls.SensorDataControl InputOne;
		SampleApp.Controls.SensorDataControl InputTwo;
		SampleApp.Controls.SensorDataControl InputThree;
		SampleApp.Controls.SensorDataControl InputFour;

		private void TryToConnect()
		{

			//ConnControl.Visibility = Visibility.Visible;

			//var conType = CreateConnection();

			_brick = new Brick(new BluetoothCommunication("COM5"), true);
			_brick.BrickChanged += _brick_BrickChanged;
			try
			{
				_brick.ConnectAsync();
				//ConnControl.Visibility = Visibility.Collapsed;

				//ConnTypeRun.Text = ConnControl.GetConnectionType().ToString();

			}
			catch (Exception)
			{
				Debug.WriteLine("Could not connect");
			}
				
				
			Debug.WriteLine("Invalid connection type for this device");

		}

		void _brick_BrickChanged(object sender, BrickChangedEventArgs e)
		{
			MotorA.Update(_brick);
			MotorB.Update(_brick);
			MotorC.Update(_brick);
			MotorD.Update(_brick);

			InputOne.Update(_brick);
			InputTwo.Update(_brick);
			InputThree.Update(_brick);
			InputFour.Update(_brick);
		}
		static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
