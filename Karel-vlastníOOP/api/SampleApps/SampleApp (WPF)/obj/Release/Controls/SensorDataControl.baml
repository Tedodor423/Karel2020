   M S B A M L   `   `   `  ����   SampleApp (WPF)*    $SampleApp.Controls.SensorDataControl   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     @d2http://schemas.microsoft.com/expression/blend/2008     -     >�Name$  ControlBody��$	��170��$��0, 0, 10, 10q����� *Width+ �� RelativeSource �� *Self+ � 	Resources    	LineStyle �� 
TargetType �� Property �� Value  HamburgerStyle �� 
TargetType'  !System.Windows.VisualStateManager   VisualStateGroups%  System.Windows.VisualStateGroup   States   System.Windows.VisualState��%,  &	        &	      7   7   7   �� " ��.��� 
 �@��X2$ 30����  �@��StrokeStartLineCap$
 Flat=���  �@��StrokeEndLineCap$
 Flat=���  � ��$ 4����  � ��$ 
0, 0, 0, 5q���  �@��Stretch$ Uniform=���  � ��
 �   ���  � ��
 �   ��� " ��.���  � ��$ 0q���  � ��$ 0q���  � �� �� " ��.R�� 
������    CommonStates��.   
Normal��  	MouseOver��  Pressed��  Disabled��.+��� $��
8, 8, 0, 0q�$	��Top=�.+��� 8��  �� 8�� �� 8�� .��� .+�� 
�������.+��� $��0, 2, 10, 10q�$��Right=�$	��Top=�.+��� $��0, 0, 0, -5q����#999$��Right=�$��20(��� -   	 ��Name$	 	MotorType��$�Unknown���� ���#999$��Right=�$��20(��� $�Port �� �� -   $	 PortName��$	�???���� -   $��SensorDataStackPanel��$��
8, 0, 0, 3q�$��Bottom=�.+��� $��0, 0, 0, -10q�$��23(�
���   ��� -   $	 RawRun��$�50���� $��8(�$� ���� ���#999$	�raw��$��20(��� $��0, 0, 0, -10q�$��23(�
���   ��� -   $	 PercentageRun��$�50���� $��8(�$� ���� ���#999$�%��$��14(��� $��23(�
���   ��� -   $	 SiRun��$�50���� $��8(�$� ���� ���#999$�Si��$��20(��� -   $��60��$
��Left=�$	��Top=�$��Center=�#��[ ���� *Width+ �� *Self+� $y�	Collapsed=�
 � RowDefinitions
 �� $��10 ��� �� $��10 � � ColumnDefinitions �� $��10 ��� �� $��10 �.+��� 
���  �� J� Opacity$ .4Q�$��0��$��3���� 
���  ��$ .4Q�$��2��$��3���� 
���  ��$ .4Q�$��0��$��3���� 
���  ��$ .4Q�$��2��$��3��