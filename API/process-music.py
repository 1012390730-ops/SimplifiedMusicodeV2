import json


def handler(request, context):
    """
    最小版本的AI音乐处理API
    先确保部署成功，后续再添加音频处理功能
    """
    # 设置CORS头
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    try:
        # 处理OPTIONS请求（预检请求）
        if request.method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers
            }

        # 处理GET请求 - 用于测试API是否正常
        elif request.method == 'GET':
            response_data = {
                'success': True,
                'message': '🎵 AI音乐API运行正常！',
                'version': '1.0.0-minimal',
                'status': '已部署，等待音频处理功能',
                'endpoints': {
                    'GET /': 'API状态检查',
                    'POST /api/process-music': '处理音频数据（开发中）'
                }
            }

            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(response_data)
            }

        # 处理POST请求 - 模拟音频处理
        elif request.method == 'POST':
            # 解析请求数据
            try:
                body = request.body
                if isinstance(body, str):
                    data = json.loads(body)
                else:
                    data = body
            except:
                data = {}

            # 检查是否有音频数据
            has_audio_data = 'audioData' in data and len(data['audioData']) > 0

            # 模拟处理结果
            response_data = {
                'success': True,
                'message': '✅ 最小版本部署成功！',
                'tempo': 120,
                'key': 'C',
                'chords': ['C', 'G', 'Am', 'F'],
                'mode': 'demo',
                'note': '当前为演示模式，后续将添加真实的音频分析功能',
                'audio_received': has_audio_data,
                'next_steps': [
                    '1. 基础部署 ✓',
                    '2. 添加音频处理库',
                    '3. 实现节奏检测',
                    '4. 实现调性识别',
                    '5. 生成伴奏音乐'
                ]
            }

            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(response_data)
            }

        else:
            return {
                'statusCode': 405,
                'headers': headers,
                'body': json.dumps({
                    'success': False,
                    'error': 'Method not allowed'
                })
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'success': False,
                'error': f'Server error: {str(e)}'
            })
        }